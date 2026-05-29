from django.db import models
from .clinic import Clinic

class Pathology_profile(models.Model):

    clinic = models.ForeignKey(
    Clinic,
    on_delete=models.CASCADE,
    related_name="profiles"
    )

    tests = models.ManyToManyField(
        "Test",
        related_name="profiles",
        blank=True
    )

    service_name = models.CharField(
        max_length=255
    )

    status = models.BooleanField(
        default=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "pathology_profiles"
        ordering = ['-id']

    def __str__(self):
        return self.service_name