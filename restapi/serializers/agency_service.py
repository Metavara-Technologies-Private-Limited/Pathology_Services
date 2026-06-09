from rest_framework import serializers
from restapi.models.agency_service import AgencyService


class AgencyServiceSerializer(serializers.ModelSerializer):

    # profile_name kept so frontend response shape stays the same
    profile_name = serializers.CharField(
        source='service_name',
        read_only=True
    )

    agency_name = serializers.CharField(
        source='agency.agency_name',
        read_only=True
    )

    class Meta:
        model = AgencyService
        fields = '__all__'
        extra_kwargs = {
            'agency': {'required': False}
        }