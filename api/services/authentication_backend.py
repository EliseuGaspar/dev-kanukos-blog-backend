"""
from backend.settings.base import SECRET_KEY
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime, timedelta
import jwt


class AuthenticationJWT:

    @classmethod
    def generateToken(cls, id: int, email: str, perm: str) -> str:
        payload = {
                'id': id,
                'email': email,
                'permission': perm,
                'exp': datetime.utcnow() + timedelta(hours=24)
            }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token

    @classmethod
    def requiredToken(cls, request: any, object_db: any):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None
        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        user = object_db.objects.get(id=payload['id'])
        return (user, token)
"""
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from api.serializers.user_serializers import UserSerializer
from api.models.primaries.admin_model import Admin
from api.serializers.admin_seriazers import AdminSerializer
from .hashPasswordFeature import HashPassword


class AuthenticationUserBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        entitie = kwargs.get('entitie')

        if entitie == 'user-login':
            return self.user_login(username, password)
        else:
            return self.admin_login(username, password)


    def user_login(self, username = None, password = None) -> any:
        UserModel = get_user_model()
        try:
            queryset = UserModel.objects.filter(email=username)
            serializer = UserSerializer(queryset, many = True)
            user = serializer.data[0]
        except UserModel.DoesNotExist:
            return None
        except IndexError:
            return None
        if HashPassword.verify(password, user.get('password')):
            return queryset
        return None


    def admin_login(self, username = None, password = None) -> any:
        UserModel = Admin
        try:
            queryset = UserModel.objects.filter(email=username)
            serializer = AdminSerializer(queryset, many = True)
            user = serializer.data[0]
        except UserModel.DoesNotExist:
            return None
        except IndexError:
            return None
        if HashPassword.verify(password, user.get('password')):
            return queryset
        return None



