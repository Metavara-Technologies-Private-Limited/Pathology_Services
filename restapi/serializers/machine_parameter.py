from rest_framework import serializers

from restapi.models.machine_parameter import (
    MachineParameter
)


class MachineParameterSerializer(
    serializers.ModelSerializer
):

    parameter_name = serializers.CharField(
        source='parameter.parameter_name',
        read_only=True
    )

    machine_name = serializers.CharField(
        source='machine.machine_name',
        read_only=True
    )

    class Meta:
        model = MachineParameter
        fields = '__all__'