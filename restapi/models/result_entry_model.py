from django.db import models
from restapi.models.receive_model import ReceiveSample


class ResultEntry(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    )

    receive_sample = models.ForeignKey(
        ReceiveSample,
        on_delete=models.CASCADE,
        related_name="result_entries"
    )

    parameter_name = models.CharField(max_length=200)
    result_value = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    entered_by = models.CharField(max_length=100, null=True, blank=True)
    result_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.receive_sample.specimen_no} - {self.parameter_name}"