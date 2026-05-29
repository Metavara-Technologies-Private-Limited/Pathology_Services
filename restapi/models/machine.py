from django.db import models
from .clinic import Clinic
import uuid

class Machine(models.Model):
    
    uuid = models.UUIDField(
    default=uuid.uuid4,
    editable=False,
    unique=True
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
        db_table = "machines"
        ordering = ['-id']

    def __str__(self):

        return self.machine_name