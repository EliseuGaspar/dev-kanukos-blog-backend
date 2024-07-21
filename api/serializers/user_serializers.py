from rest_framework.serializers import (
    ModelSerializer
)
from api.models.primaries.user_model import User

# Serializador para as rotas CRUD
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'is_active',]

# Serializador para as consultas de chaves estrangeiras
class UserSerializerToFKQ(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'name',]

# Serializador para as consultas Retrieve de usuários
class UserSerializerToRetrieve(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'user', 'email',]
