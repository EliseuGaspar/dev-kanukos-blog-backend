from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from api.models.primaries.admin_model import Admin
from api.services.jwt_middleware import JwtMiddleware
from api.services.convertors_service import Convertor
from api.serializers.admin_seriazers import AdminSerializer
from api.serializers.login_serializer import AuthLoginSerializer


class LoginViewAuthAdmin(CreateAPIView):
	serializer_class = AuthLoginSerializer
	queryset = Admin.objects.all()

	def create(self, request, *args, **kwargs):
		admin = authenticate(username=request.data.get('email'), password=request.data.get('password'))
		if admin:
			data = Convertor.convert_queryset_to_dict(admin, self, AdminSerializer)
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


