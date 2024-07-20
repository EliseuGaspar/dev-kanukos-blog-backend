from rest_framework.serializers import (
    Serializer, CharField, EmailField
)


# Seralizador para as rotas login/logout...
class AuthLoginSerializer(Serializer):

    email = EmailField()
    password = CharField()