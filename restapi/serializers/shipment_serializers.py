from rest_framework import serializers

from ..models import (
    Patient,
    PendingShipment,
    ScheduleShipping,
    ShipmentShipped,
    ShipmentReceived,
    ActivityLogs
)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class PendingShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingShipment
        fields = "__all__"


class ScheduleShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleShipping
        fields = "__all__"


class ShipmentShippedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentShipped
        fields = "__all__"


class ShipmentReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentReceived
        fields = "__all__"


class ActivityLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLogs
        fields = "__all__"