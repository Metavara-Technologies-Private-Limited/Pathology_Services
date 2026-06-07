import uuid

from django.db import models

from restapi.constants.order_status import TestStatus, TestType
from restapi.models.agency import Agency
from restapi.models.sample import Sample
from restapi.models.test_test import Test


class Collection(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    # Vidai order-level fields
    work_order_id = models.BigIntegerField(db_index=True)
    bill_number = models.CharField(max_length=100, null=True, blank=True)
    bill_type = models.CharField(max_length=50, null=True, blank=True)
    visit_id = models.BigIntegerField(null=True, blank=True)
    visit_date = models.DateField(null=True, blank=True)

    # Vidai patient-level fields
    patient_id = models.BigIntegerField(db_index=True)
    patient_name = models.CharField(max_length=255, null=True, blank=True)
    patient_mrn = models.CharField(max_length=100, null=True, blank=True)
    patient_age = models.IntegerField(null=True, blank=True)
    patient_gender = models.CharField(max_length=20, null=True, blank=True)
    patient_type = models.CharField(max_length=50, null=True, blank=True)
    cycle_number = models.CharField(max_length=100, null=True, blank=True)
    doctor_name = models.CharField(max_length=255, null=True, blank=True)

    # Vidai invoice-item level fields
    invoice_item_id = models.BigIntegerField(null=True, blank=True)
    billing_source_type = models.CharField(max_length=50, null=True, blank=True)
    billing_source_id = models.BigIntegerField(null=True, blank=True, db_index=True)
    billing_source_code = models.CharField(max_length=50, null=True, blank=True)
    billing_source_name = models.CharField(max_length=255, null=True, blank=True)
    test_service_id = models.BigIntegerField(null=True, blank=True, db_index=True)
    test_service_code = models.CharField(max_length=50, null=True, blank=True)
    test_service_name = models.CharField(max_length=255, null=True, blank=True)
    charges = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_from_package = models.BooleanField(default=False)
    is_refunded = models.BooleanField(default=False)

    # Config FKs
    test = models.ForeignKey(
        Test,
        on_delete=models.PROTECT,
        related_name="collections",
        null=True,
        blank=True,
    )
    sample = models.ForeignKey(
        Sample,
        on_delete=models.PROTECT,
        related_name="collections",
        null=True,
        blank=True,
    )
    agency = models.ForeignKey(
        Agency,
        on_delete=models.PROTECT,
        related_name="collections",
        null=True,
        blank=True,
    )
    agency_change_reason = models.TextField(null=True, blank=True)

    # Workflow
    test_type = models.CharField(
        max_length=20,
        choices=TestType.choices,
        default=TestType.INHOUSE,
        db_index=True,
    )
    status = models.CharField(
        max_length=20,
        choices=TestStatus.choices,
        default=TestStatus.PENDING,
        db_index=True,
    )

    # Generated at collection time
    barcode_value = models.CharField(max_length=100, unique=True)
    specimen_no = models.CharField(max_length=100, unique=True)

    # Collection event
    collection_date = models.DateField()
    collection_time = models.TimeField()
    collected_by_id = models.BigIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "collections"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["work_order_id", "test_service_id"]),
            models.Index(fields=["status", "test_type"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["work_order_id", "billing_source_id", "specimen_no"],
                name="unique_collection_per_order_test",
            )
        ]

    def __str__(self):
        return f"Collection {self.specimen_no} | {self.status}"