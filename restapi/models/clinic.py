from django.db import models
import uuid

class Clinic(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    clinic_name = models.CharField(
        max_length=255
    )

    is_collection_location = models.BooleanField(
        default=False
    )

    is_processing_location = models.BooleanField(
        default=False
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