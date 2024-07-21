from rest_framework.serializers import ModelSerializer
from api.models.secondary.reactions_model import Reaction



# Serializador para as rotas CRUD
class ReactionSerializer(ModelSerializer):

    class Meta:
        model = Reaction
        fields = '__all__'


# Serializador para a consulta de chaves estrangeiras
class ReactionSerializerToFKQ(ModelSerializer):

    class Meta:
        model = Reaction
        fields = ['id', 'reaction']


# Serializador para a rota pra criação
class ReactionSerializerToCreate(ModelSerializer):

    class Meta:
        model = Reaction
        fields = ['reaction', 'post']


