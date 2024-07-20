from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.models.tertiary.favorites_model import Favorite
from api.serializers.favorites_serializers import FavoriteSerializer, FavoriteSerializerToCreate
from api.services.jwt_middleware import JwtMiddleware
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


authorization_token = openapi.Parameter(
    'Authorization', in_=openapi.IN_HEADER,
    type=openapi.TYPE_STRING, required = True
)


class FavoriteView(ViewSet):

    def get_queryset(self):
        return Favorite.objects.all()

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(
        operation_description = "Retrieve a list of FavoriteSerializer instances",
        responses={200: FavoriteSerializer(many = True)},
        manual_parameters=[authorization_token,]
    )
    def list(self, request, *args, **kwargs):
        instances = self.get_queryset()
        serializer = FavoriteSerializer(instances, many=True)
        return Response(serializer.data, status = 200)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(
        operation_description = "Create a Favorite Model instance",
        request_body = FavoriteSerializerToCreate,
        responses={201: FavoriteSerializer},
        manual_parameters=[authorization_token,]
    )
    def create(self, request, *args, **kwargs):
        new_request = self.changeRequestDatas(request, kwargs.get('current_user'))
        serializer = FavoriteSerializer(data = new_request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(
        operation_description="Partially update a Model instance",
        request_body = FavoriteSerializer,
        responses={200: FavoriteSerializer}
    )
    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        model = get_object_or_404(queryset, pk=pk)
        model.delete()
        return Response(status=204)

    def changeRequestDatas(self, request: any, id: dict):
        request.data['user'] = id.get('id')
        return request

