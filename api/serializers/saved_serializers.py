from api.models.tertiary.saved_model import Saved
from rest_framework.serializers import ModelSerializer
from .posts_serializers import PostsSerializerForFavoriteAndSaved



# Serializador para as rotas CRUD
class SavedSerializer(ModelSerializer):

    class Meta:
        model = Saved
        fields = '__all__'


# Serializador para a busca de salvos por usuários
class SavedSerializerToUserRetrieve(ModelSerializer):
    post = PostsSerializerForFavoriteAndSaved(read_only = True)

    class Meta:
        model = Saved
        fields = ['id', 'post']

