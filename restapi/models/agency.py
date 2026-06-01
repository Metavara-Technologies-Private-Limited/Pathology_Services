from django.db import models
import uuid

class Agency(models.Model):
      
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    agency_code = models.CharField(
        max_length=50,
        unique=True
    )

    agency_name = models.CharField(
        max_length=255
    )

    country = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    state = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    pincode = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    address_line_1 = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    address_line_2 = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    address_line_3 = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    contact_person_1_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    contact_person_1_mobile = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    contact_person_1_email = models.EmailField(
        blank=True,
        null=True
    )

    contact_person_2_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    contact_person_2_mobile = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    contact_person_2_email = models.EmailField(
        blank=True,
        null=True
    )

    phone_no = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    fax_no = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    specialization_details = models.TextField(
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
        db_table = "agencies"
        ordering = ['-id']

    def __str__(self):

        return self.agency_name