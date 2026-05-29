from restapi.models.machine_parameter import (
    MachineParameter
)


class MachineParameterService:

    @staticmethod
    def get_all_machine_parameters():

        return MachineParameter.objects.filter(
            is_deleted=False
        ).order_by('-id')

    @staticmethod
    def get_machine_parameter_by_id(record_id):

        return MachineParameter.objects.filter(
            id=record_id,
            is_deleted=False
        ).first()

    @staticmethod
    def create_machine_parameter(
        validated_data
    ):

        return MachineParameter.objects.create(
            **validated_data
        )

    @staticmethod
    def update_machine_parameter(
        instance,
        validated_data
    ):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

    @staticmethod
    def delete_machine_parameter(instance):

        instance.is_deleted = True
        instance.save()

        return True