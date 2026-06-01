import uuid
from django.db import models
from .service import Service
from .clinic import Clinic


class Template(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    clinic = models.ForeignKey(
    Clinic,
    on_delete=models.CASCADE,
    related_name="templates",
    )

    TEMPLATE_FOR_CHOICES = [
        ("LEAD", "Lead"),
        ("PATHOLOGY", "Pathology"),
        ("RADIOLOGY", "Radiology"),
        ("EXAMINATION", "Examination"),
        ("INVESTIGATION", "Investigation"),
        ("SURGERY", "Surgery"),
        ("OUTCOME", "Outcome"),
    ]

    TEMPLATE_FORMAT_CHOICES = [
        ("TEXT", "Text"),
        ("FORM", "Form"),
    ]

    USER_TYPE_CHOICES = [
        ("PATHOLOGIST", "Pathologist"),
        ("RADIOLOGIST", "Radiologist"),
    ]

    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("BOTH", "Both"),
    ]

    template_code = models.CharField(
        max_length=50,
        unique=True
    )

    template_name = models.CharField(
        max_length=255
    )

    template_for = models.CharField(
        max_length=30,
        choices=TEMPLATE_FOR_CHOICES
    )

    service_name = models.CharField(
    max_length=255,
    blank=True,
    null=True
   )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default="BOTH"
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        null=True,
        blank=True
    )

    template_format = models.CharField(
    max_length=20,
    choices=TEMPLATE_FORMAT_CHOICES,
    null=True,
    blank=True
    )

    # For TEXT templates
    template_text = models.TextField(
        blank=True,
        null=True
    )

    # For FORM templates
    template_json = models.JSONField(
        blank=True,
        null=True
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
        db_table = "templates"
        ordering = ["-id"]

    def __str__(self):
        return self.template_name
