from rest_framework import serializers

from restapi.models.clinic import Clinic


class ClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields = "__all__"