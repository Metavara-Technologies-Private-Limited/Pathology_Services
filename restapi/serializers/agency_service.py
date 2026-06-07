from rest_framework import serializers

from restapi.models.agency_service import (
    AgencyService
)


class AgencyServiceSerializer(
    serializers.ModelSerializer
):

    agency_name = serializers.CharField(
        source='agency.agency_name',
        read_only=True
    )

    profile_name = serializers.CharField(
        source='profile.service_name',
        read_only=True
    )

    class Meta:
        model = AgencyService
        fields = '__all__'

        extra_kwargs = {
        'agency': {'required': False}
    }