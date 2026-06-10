from rest_framework import serializers
from restapi.models.authorization_models import Authorization

class AuthorizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authorization
        fields = "__all__"