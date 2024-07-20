from rest_framework.generics import CreateAPIView
from rest_framework import status
from api.serializers.login_serializer import AuthLoginSerializer
from api.models.primaries.admin_model import Admin
from api.serializers.admin_seriazers import AdminSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from api.services.jwt_middleware import JwtMiddleware


class LoginViewAuthAdmin(CreateAPIView):
	serializer_class = AuthLoginSerializer
	queryset = Admin.objects.all()

	def convert_queryset(self, queryset, Serializer = None) -> dict:
		if Serializer:
			serializer = Serializer(queryset, many = True)
			return serializer.data[0]
		serializer = self.get_serializer(queryset, many = True)
		return serializer.data[0]

	def create(self, request, *args, **kwargs):
		admin = authenticate(username=request.data.get('email'), password=request.data.get('password'))
		if admin:
			data = self.convert_queryset(admin, AdminSerializer)

			if data.get('is_super') == True:
				access = 'super'
			elif data.get('is_content') == True:
				access = 'content'
			else:
				access = 'publish'

			token = JwtMiddleware.generateToken(
				id = data.get('id'),
				email = data.get('email'),
				permission = 'admin',
				access = access
			)
			return Response({'token': token}, status = status.HTTP_200_OK)

		return Response({'error': 'Invalid credentials'}, status = status.HTTP_401_UNAUTHORIZED)

