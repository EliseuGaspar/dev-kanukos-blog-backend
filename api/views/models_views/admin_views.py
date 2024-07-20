from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from api.models.primaries.admin_model import Admin
from api.serializers.admin_seriazers import AdminSerializer
from api.services.hashPasswordFeature import HashPassword
from api.services.jwt_middleware import JwtMiddleware
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


authorization_token = openapi.Parameter(
    'Authorization', in_=openapi.IN_HEADER,
    type=openapi.TYPE_STRING, required = True
)


class AdminViews(ModelViewSet):

    serializer_class = AdminSerializer
    queryset = Admin.objects.all()

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        hashed_password = HashPassword.encript(password)
        serializer.save(password=hashed_password)

    
    def create(self, request, *args, **kwargs):
        if kwargs.get('access') != 'super':
            return Response({
                'Access denied, route to maximum admin!'
            }, status = HTTP_401_UNAUTHORIZED)
        return super().create(request, *args, **kwargs)

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def list(self, request, *args, **kwargs):
        if kwargs.get('access') != 'super':
            return Response({
                'Access denied, route to maximum admin!'
            }, status = HTTP_401_UNAUTHORIZED)
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

