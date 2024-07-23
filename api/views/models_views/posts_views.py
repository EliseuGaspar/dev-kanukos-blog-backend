from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from api.models.primaries.posts_model import Posts
from api.services.jwt_middleware import JwtMiddleware
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.parsers import MultiPartParser, FormParser
from api.serializers.posts_serializers import (
    PostsSerializer, PostsSerializerForList,
    PostsSerializerForListRetrivie,
    PostsSerializerToPATCH,
    PostStatusSerializer
)


authorization_token = openapi.Parameter(
    'Authorization', in_ = openapi.IN_HEADER,
    type = openapi.TYPE_STRING, required = False
)

status_param = openapi.Parameter(
    'status', in_ = openapi.IN_QUERY,
    type = openapi.TYPE_STRING, required = False,
    description = 'Filter posts by status (draft, published, archived)'
)


class PostsViewCrud(ModelViewSet):
    
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    parser_classes = (MultiPartParser, FormParser)

    def check_access(self, access: str, order: str) -> None | Response:
        if order == 'sup_cont':
            if access != 'super' and access != 'content':
                return Response({
                    'Access denied, route to maximum admin and content admin!'
                }, status = HTTP_401_UNAUTHORIZED)
            else:
                return
        if access != 'super' and access != 'publish':
            return Response({
                'Access denied, route to maximum admin and publish admin!'
            }, status = HTTP_401_UNAUTHORIZED)
        return

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def create(self, request, *args, **kwargs):
        access = self.check_access(kwargs.get('access'), 'sup_cont')
        if isinstance(access, Response):
            return access
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[authorization_token, status_param,])
    def list(self, request, *args, **kwargs):
        status = request.query_params.get('status', 'published')
        if status == 'published':
            queryset = Posts.objects.filter(status = status)
            serializer = PostsSerializerForList(queryset, many = True)
            return Response(serializer.data, status = 200)
        else:
            access = JwtMiddleware.verifyToken(request.headers.get('Authorization'))
            if access == True:
                queryset = Posts.objects.filter(status = status)
                serializer = PostsSerializerForList(queryset, many = True)
                return Response(serializer.data, status = 200)
            return access

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def retrieve(self, request, pk = None, *args, **kwargs):
        queryset = Posts.objects.select_related('author').prefetch_related('comments__user', 'reactions')
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostsSerializerForListRetrivie(post)
        return Response(serializer.data)

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(
        manual_parameters=[authorization_token,],
        request_body = PostsSerializerToPATCH,
    )
    def update(self, request, *args, **kwargs):
        access = self.check_access(kwargs.get('access'), 'sup_cont')
        if isinstance(access, Response):
            return access
        return super().update(request, *args, **kwargs)

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(
        manual_parameters=[authorization_token,],
        request_body = PostsSerializerToPATCH
    )
    def partial_update(self, request, *args, **kwargs):
        access = self.check_access(kwargs.get('access'), 'sup_cont')
        if isinstance(access, Response):
            return access
        return super().partial_update(request, *args, **kwargs)

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def destroy(self, request, *args, **kwargs):
        self.check_access(kwargs.get('access'))
        return super().destroy(request, *args, **kwargs)

    @JwtMiddleware.adminAccessOnly
    @action(detail = True, methods=['patch'], url_path='update-status')
    @swagger_auto_schema(
        manual_parameters=[authorization_token],
        request_body=PostStatusSerializer
    )
    def update_status(self, request, pk=None, *args, **kwargs):
        access = self.check_access(kwargs.get('access'), 'sup_pub')
        if isinstance(access, Response):
            return access
        post = self.get_object()
        serializer = PostStatusSerializer(data=request.data)
        if serializer.is_valid():
            post.status = serializer.validated_data['status']
            post.save()
            return Response({'status': 'status updated'}, status = 200)
        else:
            return Response(serializer.errors, status = 400)

