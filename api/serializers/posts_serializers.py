from rest_framework.serializers import ModelSerializer
from api.models.primaries.posts_model import Posts
from .comments_serializers import CommentsSerializerToFKQ
from .reactions_serializers import ReactionSerializerToFKQ
from .admin_seriazers import AdminSerializerToFKQ

# Serializador para as rotas CRUD
class PostsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ['title', 'header', 'body', 'author', 'status', 'category', 'comments_enabled', 'cover', 'midia']


class PostsSerializerForList(ModelSerializer):
    author = AdminSerializerToFKQ(read_only = True)

    class Meta:
        model = Posts
        fields = ['id', 'title', 'header', 'body', 'author', 'status', 'category', 'comments_enabled', 'cover', 'midia']


class PostsSerializerForListRetrivie(ModelSerializer):
    comments = CommentsSerializerToFKQ(many = True, read_only = True)
    reactions = ReactionSerializerToFKQ(many = True, read_only = True)
    author = AdminSerializerToFKQ(read_only = True)

    class Meta:
        model = Posts
        fields = '__all__'


class PostsSerializerForFavoriteAndSaved(ModelSerializer):

    class Meta:
        model = Posts
        fields = ['id', 'title', 'header', 'cover']



