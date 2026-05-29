from restapi.models.machine import Machine


class MachineService:

    @staticmethod
    def get_all_machines():

        return Machine.objects.filter(
            is_deleted=False
        ).order_by('-id')

    @staticmethod
    def get_machine_by_id(machine_id):

        return Machine.objects.filter(
            id=machine_id,
            is_deleted=False
        ).first()

    @staticmethod
    def create_machine(validated_data):

        return Machine.objects.create(
            **validated_data
        )

    @staticmethod
    def update_machine(instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

    @staticmethod
    def delete_machine(instance):

        instance.is_deleted = True
        instance.save()

        return True