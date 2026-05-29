from django.db import models
import uuid

class Tube(models.Model):

    uuid = models.UUIDField(
    default=uuid.uuid4,
    editable=False,
    unique=True
   )

    tube_code=models.CharField(max_length=50, unique=True)
    tube_name=models.CharField(max_length=100)
    status=models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tube_name

    class meta:
        db_table = "tube"