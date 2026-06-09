from restapi.models.agency_clinic import (
    AgencyClinic
)


class AgencyClinicService:

    @staticmethod
    def get_all():

        return AgencyClinic.objects.filter(
            is_deleted=False
        )

    @staticmethod
    def get_by_id(pk):

        try:

            return AgencyClinic.objects.get(
                pk=pk,
                is_deleted=False
            )

        except AgencyClinic.DoesNotExist:

            return None

    @staticmethod
    def create(validated_data):

        return AgencyClinic.objects.create(
            **validated_data
        )

    @staticmethod
    def update(instance, validated_data):

        for attr, value in validated_data.items():

            setattr(instance, attr, value)

        instance.save()

        return instance

    @staticmethod
    def delete(instance):

        instance.is_deleted = True

        instance.save()