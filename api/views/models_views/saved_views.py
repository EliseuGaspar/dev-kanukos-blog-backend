from drf_yasg import openapi
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from api.models.tertiary.saved_model import Saved
from api.services.jwt_middleware import JwtMiddleware
from api.serializers.saved_serializers import SavedSerializer


authorization_token = openapi.Parameter(
    'Authorization', in_=openapi.IN_HEADER,
    type=openapi.TYPE_STRING, required = True
)


class SavedView(ViewSet):

    def get_queryset(self):
        return Saved.objects.all()

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(
        operation_description = "Retrieve a list of SavedSerializer instances",
        responses={200: SavedSerializer(many = True)},
        manual_parameters=[authorization_token,]
    )
    def list(self, request, *args, **kwargs):
        instances = self.get_queryset()
        serializer = SavedSerializer(instances, many=True)
        return Response(serializer.data, status = 200)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(
        operation_description = "Retrieve a list of SavedSerializer instances",
        responses={200: SavedSerializer},
        manual_parameters=[authorization_token,]
    )
    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        model = get_object_or_404(queryset, pk=pk)
        serializer = SavedSerializer(model)
        return Response(serializer.data)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(
        operation_description = "Create a Saved Model instance",
        request_body = SavedSerializer,
        responses={201: SavedSerializer},
        manual_parameters=[authorization_token,]
    )
    def create(self, request, *args, **kwargs):
        serializer = SavedSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(
        operation_description="Partially update a Saved Model instance",
        request_body = SavedSerializer,
        responses={200: SavedSerializer}
    )
    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        model = get_object_or_404(queryset, pk=pk)
        model.delete()
        return Response(status=204)
