from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from api.models.primaries.posts_model import Posts
from api.serializers.posts_serializers import PostsSerializer, PostsSerializerForList, PostsSerializerForListRetrivie
from api.services.jwt_middleware import JwtMiddleware
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


authorization_token = openapi.Parameter(
    'Authorization', in_=openapi.IN_HEADER,
    type=openapi.TYPE_STRING, required = True
)


class PostsViewCrud(ModelViewSet):
    
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    parser_classes = (MultiPartParser, FormParser)

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def create(self, request, *args, **kwargs):
        if kwargs.get('access') != 'super' and kwargs.get('access') != 'content':
            return Response({
                'Access denied, route to maximum admin and content admin!'
            }, status = HTTP_401_UNAUTHORIZED)
        return super().create(request, *args, **kwargs)

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def list(self, request, *args, **kwargs):
        queryset = Posts.objects.all()
        serializer = PostsSerializerForList(queryset, many=True)
        return Response(serializer.data, status = 200)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def retrieve(self, request, pk = None, *args, **kwargs):
        queryset = Posts.objects.select_related('author').prefetch_related('comments__user', 'reactions')
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostsSerializerForListRetrivie(post)
        return Response(serializer.data)

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def update(self, request, *args, **kwargs):
        if kwargs.get('access') != 'super' or kwargs.get('access') != 'content':
            return Response({
                'Access denied, route to maximum admin and content admin!'
            }, status = HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def partial_update(self, request, *args, **kwargs):
        if kwargs.get('access') != 'super' or kwargs.get('access') != 'content':
            return Response({
                'Access denied, route to maximum admin and content admin!'
            }, status = HTTP_401_UNAUTHORIZED)
        return super().partial_update(request, *args, **kwargs)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def destroy(self, request, *args, **kwargs):
        if kwargs.get('access') != 'super' or kwargs.get('access') != 'publish':
            return Response({
                'Access denied, route to maximum admin and publish admin!'
            }, status = HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)