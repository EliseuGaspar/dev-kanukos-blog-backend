from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from api.services.jwt_middleware import JwtMiddleware
from api.models.secondary.comments_model import Comments
from api.serializers.comments_serializers import CommentsSerializer


authorization_token = openapi.Parameter(
    'Authorization', in_=openapi.IN_HEADER,
    type=openapi.TYPE_STRING, required = True
)


class CommentsViewCrud(ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(manual_parameters=[authorization_token,])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

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