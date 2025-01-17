from rest_framework.serializers import ModelSerializer, IntegerField
from api.models.tertiary.favorites_model import Favorite
from .posts_serializers import PostsSerializerForFavoriteAndSaved



# Serializador para as rotas CRUD
class FavoriteSerializer(ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteSerializerToCreate(ModelSerializer):
    user = IntegerField(required = False)

    class Meta:
        model = Favorite
        fields = ['post', 'user']


class FavoriteSerializerToUserRetrieve(ModelSerializer):
    post = PostsSerializerForFavoriteAndSaved(read_only = True)

    class Meta:
        model = Favorite
        fields = ['id', 'post']


