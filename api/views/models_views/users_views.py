from rest_framework.viewsets import ModelViewSet
from api.models.primaries.user_model import User
from api.models.tertiary.favorites_model import Favorite
from api.models.tertiary.saved_model import Saved
from api.serializers.user_serializers import UserSerializer
from api.serializers.favorites_serializers import FavoriteSerializerToUserRetrieve
from api.serializers.saved_serializers import SavedSerializerToUserRetrieve
from api.services.hashPasswordFeature import HashPassword
from api.services.jwt_middleware import JwtMiddleware
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg import openapi


authorization_token = openapi.Parameter(
    'Authorization', in_=openapi.IN_HEADER,
    type=openapi.TYPE_STRING, required = True
)


class UserViewsCrud(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        hashed_password = HashPassword.encript(password)
        serializer.save(password=hashed_password)

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    @action(detail = False, methods = ['GET'])
    def get_favorites(self, request, *args, **kwargs):
        id = kwargs.get('current_user')
        queryset = Favorite.objects.filter(user = id.get('id'))
        serializer = FavoriteSerializerToUserRetrieve(queryset, many = True)
        return Response(serializer.data, status = 200)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    @action(detail = False, methods = ['GET'])
    def get_saved(self, request, *args, **kwargs):
        id = kwargs.get('current_user')
        queryset = Saved.objects.filter(user = id.get('id'))
        serializer = SavedSerializerToUserRetrieve(queryset, many = True)
        return Response(serializer.data, status = 200)
