from rest_framework import serializers
from restapi.models.result_entry_model import ResultEntry


class ResultEntrySerializer(serializers.ModelSerializer):
    specimen_no = serializers.CharField(source="receive_sample.specimen_no", read_only=True)
    shipment_no = serializers.CharField(source="receive_sample.shipment_no", read_only=True)
    patient_name = serializers.CharField(source="receive_sample.patient_name", read_only=True)
    test_name = serializers.CharField(source="receive_sample.test_name", read_only=True)
    patient_age = serializers.IntegerField(
        source="receive_sample.patient_age",
        read_only=True
    )

    patient_gender = serializers.CharField(
        source="receive_sample.patient_gender",
        read_only=True
    )

    patient_code = serializers.CharField(
        source="receive_sample.patient_code",
        read_only=True
    )

    service_name = serializers.CharField(
        source="receive_sample.service_name",
        read_only=True
    )

    class Meta:
        model = ResultEntry
        fields = "__all__"