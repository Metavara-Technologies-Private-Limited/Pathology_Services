from django.db import models
from .clinic import Clinic
import uuid

class Tube(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    clinic = models.ForeignKey(
    Clinic,
    on_delete=models.CASCADE,
    related_name="tubes",
    )
    
    tube_code=models.CharField(max_length=50, unique=True)
    tube_name=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.tube_name

    class meta:
        db_table = "tube"