from django.db import models
import uuid
from restapi.models.machine import Machine


class MachineParameter(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    machine_parameter_code = models.CharField(
        max_length=50,
        unique=True
    )

    machine_parameter_name = models.CharField(
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
        db_table = "machine_parameters"
        ordering = ['-id']

    def __str__(self):

        return self.machine_parameter_name