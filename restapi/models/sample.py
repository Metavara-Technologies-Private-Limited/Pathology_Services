from django.db import models
import uuid

class Sample(models.Model):

    uuid = models.UUIDField(
    default=uuid.uuid4,
    editable=False,
    unique=True
    )
    sample_code= models.CharField(max_length=50, unique=True)
    sample_name= models.CharField(max_length= 100)
    status= models.BooleanField(default=True)
    frequency = models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sample_name
    class meta:
        db_table = "sample"
