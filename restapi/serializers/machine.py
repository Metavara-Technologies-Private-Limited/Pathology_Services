from rest_framework import serializers
from restapi.models.machine_parameter import MachineParameter
from restapi.models.machine import Machine


class MachineSerializer(serializers.ModelSerializer):

    clinic_name = serializers.CharField(
        source='clinic.clinic_name',
        read_only=True
    )

    machine_parameters = serializers.PrimaryKeyRelatedField(
        queryset=MachineParameter.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Machine
        fields = [
            'id',
            'clinic',
            'clinic_name',
            'machine_code',
            'machine_name',
            'machine_parameters',
            'status',
            'is_deleted',
            'created_at',
            'updated_at',
        ]