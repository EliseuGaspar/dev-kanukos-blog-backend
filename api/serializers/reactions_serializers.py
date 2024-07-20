from rest_framework.serializers import ModelSerializer
from api.models.secondary.reactions_model import Reaction


# Serializador para as rotas CRUD
class ReactionSerializer(ModelSerializer):

    class Meta:
        model = Reaction
        fields = '__all__'


class ReactionSerializerToFKQ(ModelSerializer):

    class Meta:
        model = Reaction
        fields = ['id', 'reaction']

class ReactionSerializerToCreate(ModelSerializer):

    class Meta:
        model = Reaction
        fields = ['reaction', 'post']


