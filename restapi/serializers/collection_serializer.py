from rest_framework import serializers

from restapi.constants.order_status import (
    TestStatus,
    TestType,
)
from restapi.models.collection import Collection


class CollectionSerializer(serializers.ModelSerializer):

    status_display = serializers.CharField(
        source="get_status_display",
        read_only=True,
    )
    test_type_display = serializers.CharField(
        source="get_test_type_display",
        read_only=True,
    )

    # Derived from test FK
    test_name = serializers.CharField(
        source="test.test_name",
        read_only=True,
    )
    test_code = serializers.CharField(
        source="test.test_code",
        read_only=True,
    )
    service_name = serializers.CharField(
        source="test.service_name",
        read_only=True,
    )
    tube_name = serializers.CharField(
        source="test.tube_name.tube_name",
        read_only=True,
    )

    # Derived from sample FK
    sample_name = serializers.CharField(
        source="sample.sample_name",
        read_only=True,
    )
    sample_code = serializers.CharField(
        source="sample.sample_code",
        read_only=True,
    )

    # Derived from agency FK
    agency_name = serializers.CharField(
        source="agency.agency_name",
        read_only=True,
    )

    class Meta:
        model = Collection

        fields = [
            "id",

            # Vidai order-level
            "work_order_id",
            "bill_number",
            "bill_type",
            "visit_id",
            "visit_date",

            # Vidai patient-level
            "patient_id",
            "patient_name",
            "patient_mrn",
            "patient_age",
            "patient_gender",
            "patient_type",
            "cycle_number",
            "doctor_name",

            # Vidai invoice-item level
            "invoice_item_id",
            "billing_source_type",
            "billing_source_id",
            "billing_source_code",
            "billing_source_name",
            "test_service_id",
            "test_service_code",
            "test_service_name",
            "charges",
            "net_amount",
            "is_from_package",
            "is_refunded",

            # Config FKs + derived fields
            "test",
            "test_code",
            "test_name",
            "service_name",
            "tube_name",

            "sample",
            "sample_code",
            "sample_name",

            "agency",
            "agency_name",
            "agency_change_reason",

            # Workflow
            "test_type",
            "test_type_display",
            "status",
            "status_display",

            # Generated
            "barcode_value",
            "specimen_no",

            # Collection event
            "collection_date",
            "collection_time",
            "collected_by_id",

            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "status",
            "barcode_value",
            "specimen_no",
            "agency_change_reason",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        test_type = attrs.get(
            "test_type",
            getattr(self.instance, "test_type", None),
        )
        agency = attrs.get(
            "agency",
            getattr(self.instance, "agency", None),
        )

        if test_type == TestType.OUTSOURCE and agency is None:
            raise serializers.ValidationError(
                {"agency": "Agency is required for outsourced collections."}
            )

        return attrs


class GenerateCollectionBarcodeSerializer(serializers.Serializer):
    barcode_value = serializers.CharField(read_only=True)
    specimen_no = serializers.CharField(read_only=True)


class UpdateCollectionStatusSerializer(serializers.Serializer):
    new_status = serializers.ChoiceField(choices=TestStatus.choices)


class ChangeCollectionAgencySerializer(serializers.Serializer):
    new_agency_id = serializers.UUIDField()
    reason = serializers.CharField(max_length=500)

    def validate_reason(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Reason cannot be blank."
            )
        return value