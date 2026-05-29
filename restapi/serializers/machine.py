from rest_framework import serializers
from restapi.models.machine import Machine


class MachineSerializer(serializers.ModelSerializer):

    clinic_name = serializers.CharField(
        source='clinic.clinic_name',
        read_only=True
    )

    class Meta:
        model = Machine
        fields = [
            'id',
            'uuid',
            'clinic',
            'clinic_name',
            'machine_code',
            'machine_name',
            'status',
            'is_deleted',
            'created_at',
            'updated_at',
        ]