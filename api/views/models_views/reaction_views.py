from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.models.secondary.reactions_model import Reaction
from api.serializers.reactions_serializers import ReactionSerializer, ReactionSerializerToCreate
from api.services.jwt_middleware import JwtMiddleware
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


authorization_token = openapi.Parameter(
    'Authorization', in_=openapi.IN_HEADER,
    type=openapi.TYPE_STRING, required = True
)


class ReactionsView(ViewSet):

    def get_queryset(self):
        return Reaction.objects.all()

    @JwtMiddleware.adminAccessOnly
    @swagger_auto_schema(
        operation_description = "Retrieve a list of ReactionSerializer instances",
        responses={200: ReactionSerializer(many = True)},
        manual_parameters=[authorization_token,]
    )
    def list(self, request, *args, **kwargs):
        instances = self.get_queryset()
        serializer = ReactionSerializer(instances, many=True)
        return Response(serializer.data, status = 200)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(
        operation_description = "Create a Reaction Model instance",
        request_body = ReactionSerializerToCreate,
        responses={201: ReactionSerializer},
        manual_parameters=[authorization_token,]
    )
    def create(self, request, *args, **kwargs):
        new_request = self.changeRequestDatas(request, kwargs.get('current_user'))
        serializer = ReactionSerializer(data = new_request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    @JwtMiddleware.tokenRequired
    @swagger_auto_schema(
        operation_description="Partially update a MyModel instance",
        request_body = ReactionSerializer,
        responses={200: ReactionSerializer}
    )
    def partial_update(self, request, pk=None):
        queryset = self.get_queryset()
        mymodel = get_object_or_404(queryset, pk=pk)
        serializer = ReactionSerializer(mymodel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.errors, status=400)

    def changeRequestDatas(self, request: any, id: dict):
        request.data['user'] = id.get('id')
        return request

