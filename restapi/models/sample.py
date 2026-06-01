from django.db import models
from .clinic import Clinic
import uuid

class Sample(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    clinic = models.ForeignKey(
    Clinic,
    on_delete=models.CASCADE,
    related_name="samples",
    )

    sample_code= models.CharField(max_length=50, unique=True)
    sample_name= models.CharField(max_length= 100)
    status= models.BooleanField(default=True)
    frequency = models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.sample_name
    class meta:
        db_table = "sample"
