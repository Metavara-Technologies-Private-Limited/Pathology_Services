from rest_framework import serializers
from restapi.models.receive_model import ReceiveSample


class ReceiveSampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReceiveSample
        fields = "__all__"       