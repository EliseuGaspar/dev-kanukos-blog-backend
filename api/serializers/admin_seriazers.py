from rest_framework.serializers import ModelSerializer
from api.models.primaries.admin_model import Admin


# Serializador para as rotas CRUD
class AdminSerializer(ModelSerializer):

    class Meta:
        model = Admin
        fields = ['id', 'name', 'email', 'password', 'is_super', 'is_content', 'is_pub']


class AdminSerializerToFKQ(ModelSerializer):

    class Meta:
        model = Admin
        fields = ['id', 'name']



