from .admin_seriazers import AdminSerializerToFKQ
from api.models.primaries.posts_model import Posts
from rest_framework.serializers import (
    ModelSerializer, CharField, FileField,
    IntegerField, BooleanField, Serializer,
    ChoiceField)
from .comments_serializers import CommentsSerializerToFKQ
from .reactions_serializers import ReactionSerializerToFKQ



# Serializador para as rotas CRUD
class PostsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ['title', 'header', 'body', 'author', 'status', 'category', 'comments_enabled', 'cover', 'midia']


class PostStatusSerializer(Serializer):
    status = ChoiceField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')])


class PostsSerializerToPATCH(ModelSerializer):
    title = CharField(required = False)
    header = CharField(required = False)
    body = CharField(style={'base_template': 'textarea.html'}, required = False)
    author = IntegerField(required = False)
    category = CharField(required = False)
    comments_enabled = BooleanField(required = False)
    cover = FileField(required = False)
    midia = FileField(required = False)

    class Meta:
        model = Posts
        fields = ['title', 'header', 'body', 'author', 'status', 'category', 'comments_enabled', 'cover', 'midia']

# Serializador para a busca sem filtros
class PostsSerializerForList(ModelSerializer):
    author = AdminSerializerToFKQ(read_only = True)

    class Meta:
        model = Posts
        fields = ['id', 'title', 'header', 'body', 'author', 'status', 'category', 'comments_enabled', 'cover', 'midia']


# Serializador para a busca com filtros
class PostsSerializerForListRetrivie(ModelSerializer):
    comments = CommentsSerializerToFKQ(many = True, read_only = True)
    reactions = ReactionSerializerToFKQ(many = True, read_only = True)
    author = AdminSerializerToFKQ(read_only = True)

    class Meta:
        model = Posts
        fields = '__all__'

# Serializador para a busca de favoritos e salvos
class PostsSerializerForFavoriteAndSaved(ModelSerializer):

    class Meta:
        model = Posts
        fields = ['id', 'title', 'header', 'cover']



