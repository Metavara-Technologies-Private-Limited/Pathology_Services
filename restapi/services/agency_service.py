from restapi.models.agency import Agency


class AgencyService:

    @staticmethod
    def get_all_agencies():

        return Agency.objects.filter(
            is_deleted=False
        ).order_by('-id')

    @staticmethod
    def get_agency_by_id(agency_id):

        return Agency.objects.filter(
            id=agency_id,
            is_deleted=False
        ).first()

    @staticmethod
    def create_agency(validated_data):

        return Agency.objects.create(
            **validated_data
        )

    @staticmethod
    def update_agency(instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

    @staticmethod
    def delete_agency(instance):

        instance.is_deleted = True
        instance.save()

        return True