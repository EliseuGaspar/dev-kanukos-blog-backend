from .hashPassword_service import HashPassword
from django.contrib.auth import get_user_model
from api.models.primaries.admin_model import Admin
from django.contrib.auth.backends import ModelBackend
from api.serializers.user_serializers import UserSerializer
from api.serializers.admin_seriazers import AdminSerializer


class AuthenticationUser(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        entitie = kwargs.get('entitie')
        if entitie == 'user-login':
            entitie = None
            return self.user_login(username, password)
        else:
            entitie = None
            return self.admin_login(username, password)


    def user_login(self, username = None, password = None) -> any:
        UserModel = get_user_model()
        try:
            queryset = UserModel.objects.filter(email=username)
            serializer = UserSerializer(queryset, many = True)
            user = serializer.data[0]
            if HashPassword.verify(password, user.get('password')):
                return queryset
        except UserModel.DoesNotExist: return None
        except IndexError: return None
        except: return None


    def admin_login(self, username = None, password = None) -> any:
        AdminModel = Admin
        try:
            queryset = AdminModel.objects.filter(email=username)
            serializer = AdminSerializer(queryset, many = True)
            admin = serializer.data[0]
            if HashPassword.verify(password, admin.get('password')):
                return queryset
        except AdminModel.DoesNotExist: return None
        except IndexError: return None
        except: return None

