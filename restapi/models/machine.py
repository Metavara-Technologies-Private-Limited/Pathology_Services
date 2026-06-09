from django.db import models
from .clinic import Clinic
import uuid

class Machine(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE,
        related_name="machines"
    )

    machine_code = models.CharField(
        max_length=50,
        unique=True
    )

    machine_name = models.CharField(
        max_length=255
    )

    machine_parameters = models.ManyToManyField(
        'MachineParameter',
        related_name='machines',
        blank=True
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