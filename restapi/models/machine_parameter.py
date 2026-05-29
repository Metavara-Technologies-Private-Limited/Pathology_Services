from django.db import models
import uuid
from restapi.models.machine import Machine
from restapi.models.test_parameter import Parameter


class MachineParameter(models.Model):

    uuid = models.UUIDField(
    default=uuid.uuid4,
    editable=False,
    unique=True
)

    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name='machine_parameters'
    )

    parameter = models.ForeignKey(
        Parameter,
        on_delete=models.CASCADE,
        related_name='parameter_machines'
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

        return (
            f"{self.machine.machine_name} - "
            f"{self.parameter.parameter_name}"
        )