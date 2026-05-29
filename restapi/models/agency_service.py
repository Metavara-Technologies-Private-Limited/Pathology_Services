from django.db import models

from restapi.models.agency import Agency
from restapi.models.pathology_profile import (
    Pathology_profile
)


class AgencyService(models.Model):

    agency = models.ForeignKey(
        Agency,
        on_delete=models.CASCADE,
        related_name='agency_services'
    )

    profile = models.ForeignKey(
        Pathology_profile,
        on_delete=models.CASCADE,
        related_name='profile_agencies'
    )

    rate = models.DecimalField(
        max_digits=10,
        decimal_places=2
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
        db_table = "agency_services"
        ordering = ['-id']

    def __str__(self):

        return (
            f"{self.agency.agency_name} - "
            f"{self.profile.service_name}"
        )