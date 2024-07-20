from rest_framework.serializers import ModelSerializer
from api.models.secondary.views_model import Views


# Serializador para as rotas CRUD
class ViewsSerializer(ModelSerializer):

    class Meta:
        model = Views
        fields = '__all__'


