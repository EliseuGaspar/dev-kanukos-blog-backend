from rest_framework.generics import CreateAPIView
from rest_framework import status
from api.serializers.login_serializer import AuthLoginSerializer
from api.serializers.user_serializers import UserSerializer
from api.models.primaries.user_model import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from api.services.jwt_middleware import JwtMiddleware


class LoginViewAuthUser(CreateAPIView):
	serializer_class = AuthLoginSerializer
	queryset = User.objects.all()

	def convert_queryset(self, queryset, Serializer = None) -> dict:
		if Serializer:
			serializer = Serializer(queryset, many = True)
			return serializer.data[0]
		serializer = self.get_serializer(queryset, many = True)
		return serializer.data[0]

	def create(self, request, *args, **kwargs):
		user = authenticate(username=request.data.get('email'), password=request.data.get('password'), entitie = 'user-login')
		if user:
			data = self.convert_queryset(user, UserSerializer)

			token = JwtMiddleware.generateToken(
				id = data.get('id'),
				email = data.get('email'),
				permission = 'user'
			)
			return Response({'token': token}, status = status.HTTP_200_OK)

		return Response({'error': 'Invalid credentials'}, status = status.HTTP_401_UNAUTHORIZED)

