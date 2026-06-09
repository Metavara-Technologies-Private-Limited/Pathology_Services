from restapi.models.clinic import Clinic


class ClinicService:

    @staticmethod
    def get_all_clinics():

        return Clinic.objects.filter(
            is_deleted=False
        )

    @staticmethod
    def get_clinic_by_id(pk):

        try:
            return Clinic.objects.get(
                pk=pk,
                is_deleted=False
            )

        except Clinic.DoesNotExist:
            return None

    @staticmethod
    def create_clinic(validated_data):

        return Clinic.objects.create(
            **validated_data
        )

    @staticmethod
    def update_clinic(instance, validated_data):

        for attr, value in validated_data.items():

            setattr(instance, attr, value)

        instance.save()

        return instance

    @staticmethod
    def delete_clinic(instance):

        instance.is_deleted = True
        instance.save()