# Receive section model
from django.db import models
from .shipment import ShipmentReceived


class ReceiveSample(models.Model):

    shipment = models.ForeignKey(
        ShipmentReceived,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="receive_samples"
    )
    
    ship_date = models.DateField()

    ship_time = models.TimeField()

    shipment_no = models.CharField(max_length=100)

    specimen_no = models.CharField(max_length=100)

    specimen_type = models.CharField(max_length=100)

    test_code = models.CharField(max_length=100)

    test_name = models.CharField(max_length=100)

    service_name = models.CharField(max_length=200)

    patient_name = models.CharField(max_length=200)

    patient_age = models.IntegerField()

    patient_gender = models.CharField(max_length=20)

    patient_code = models.CharField(max_length=100)

    receive_date = models.DateField(null=True, blank=True)

    receive_time = models.TimeField(null=True, blank=True)

    accepted_by = models.CharField(max_length=100, null=True, blank=True)

    rejected_by = models.CharField(max_length=100, null=True, blank=True)

    resend_new_sample = models.BooleanField(default=False)

    remark = models.TextField(null=True, blank=True)

    sub_optimal = models.BooleanField(default=False)

    resend_new_sample = models.BooleanField(default=False)

    status = models.CharField(max_length=50, default="Shipped")

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.patient_name