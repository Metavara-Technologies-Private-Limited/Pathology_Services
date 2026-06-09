from rest_framework import serializers
from restapi.models.machine_parameter import (MachineParameter)


class MachineParameterSerializer(serializers.ModelSerializer):

    number_of_machines = serializers.SerializerMethodField()

    class Meta:

        model = MachineParameter

        fields = [
            'id',
            'machine_parameter_code',
            'machine_parameter_name',
            'number_of_machines',
            'status',
            'is_deleted',
            'created_at',
            'updated_at',
        ]

    def get_number_of_machines(
        self,
        obj
    ):

        return obj.machines.count()