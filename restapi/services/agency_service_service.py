from restapi.models.agency_service import (
    AgencyService
)


class AgencyServiceService:

    @staticmethod
    def get_all_agency_services():

        return AgencyService.objects.filter(
            is_deleted=False
        ).order_by('-id')

    @staticmethod
    def get_agency_service_by_id(record_id):

        return AgencyService.objects.filter(
            id=record_id,
            is_deleted=False
        ).first()

    @staticmethod
    def create_agency_service(
        validated_data
    ):

        return AgencyService.objects.create(
            **validated_data
        )

    @staticmethod
    def update_agency_service(
        instance,
        validated_data
    ):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

    @staticmethod
    def delete_agency_service(instance):

        instance.is_deleted = True
        instance.save()

        return True