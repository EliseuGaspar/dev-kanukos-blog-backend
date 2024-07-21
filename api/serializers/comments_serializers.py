from rest_framework.serializers import ModelSerializer
from api.models.secondary.comments_model import Comments
from .user_serializers import UserSerializerToFKQ

# Serializador para as rotas CRUD
class CommentsSerializer(ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'

# Serializador para consultas por chaves estrangeiras
class CommentsSerializerToFKQ(ModelSerializer):

    user = UserSerializerToFKQ(read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'content', 'user']
