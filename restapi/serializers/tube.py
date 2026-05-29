from rest_framework import serializers
from restapi.models.tube import Tube

class TubeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tube
        fields='__all__'