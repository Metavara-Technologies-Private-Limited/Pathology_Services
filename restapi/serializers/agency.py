from rest_framework import serializers
from restapi.models.agency import Agency
from restapi.models.agency_service import AgencyService
from restapi.serializers.agency_service import (AgencyServiceSerializer)


class AgencySerializer(serializers.ModelSerializer):

    agency_services = AgencyServiceSerializer(
    many=True,
    required=False
    )

    class Meta:
        model = Agency
        fields = '__all__'

    def create(self, validated_data):

        agency_services_data = validated_data.pop(
        'agency_services',
        []
    )

        agency = Agency.objects.create(
        **validated_data
    )

        for service_data in agency_services_data:

         AgencyService.objects.create(
            agency=agency,
            **service_data
        )

        return agency
    

    def update(self, instance, validated_data):

        agency_services_data = validated_data.pop(
        'agency_services',
        []
    )

        for attr, value in validated_data.items():

            setattr(
            instance,
            attr,
            value
        )

        instance.save()

        instance.agency_services.all().delete()

        for service_data in agency_services_data:

            AgencyService.objects.create(
            agency=instance,
            **service_data
        )

        return instance