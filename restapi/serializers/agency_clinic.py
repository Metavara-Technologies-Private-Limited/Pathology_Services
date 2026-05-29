from rest_framework import serializers

from restapi.models.agency_clinic import (
    AgencyClinic
)


class AgencyClinicSerializer(
    serializers.ModelSerializer
):

    clinic_name = serializers.CharField(
        source="clinic.clinic_name",
        read_only=True
    )

    agency_name = serializers.CharField(
        source="agency.agency_name",
        read_only=True
    )

    class Meta:

        model = AgencyClinic

        fields = "__all__"