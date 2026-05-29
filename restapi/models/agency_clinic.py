from django.db import models

from restapi.models.agency import Agency
from restapi.models.clinic import Clinic


class AgencyClinic(models.Model):

    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE,
        related_name="agency_links"
    )

    agency = models.ForeignKey(
        Agency,
        on_delete=models.CASCADE,
        related_name="clinic_links"
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

        db_table = "agency_clinics"

    def __str__(self):

        return f"{self.clinic} - {self.agency}"