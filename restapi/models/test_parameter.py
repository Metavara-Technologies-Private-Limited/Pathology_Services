from django.db import models
import uuid

class Parameter(models.Model):

    uuid = models.UUIDField(
    default=uuid.uuid4,
    editable=False,
    unique=True
    )

    TYPE_CHOICES = [
        ('NUMERIC', 'Numeric'),
        ('TEXT', 'Text'),
    ]

    UNIT_CHOICES = [
        ('mg_dl', 'mg/dL'),
        ('g_dl', 'g/dL'),
        ('ml', 'mL'),
        ('mmol_l', 'mmol/L'),
        ('percent', '%'),
    ]

    parameter_code = models.CharField(
        max_length=50,
        unique=True,
        db_index=True
    )

    parameter_name = models.CharField(
        max_length=255
    )

    parameter_print_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    type_of_value = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    unit = models.CharField(max_length=50, choices=UNIT_CHOICES )

    delta_check_percentage = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    technique_used = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    execution_calendar_linking = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    formula = models.TextField(
        blank=True,
        null=True
    )

    skip_numeric_result_entry = models.BooleanField(default=False)

    status = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "parameters"
        ordering = ['-id']

    def __str__(self):
        return self.parameter_name


class ParameterReferenceRange(models.Model):

    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('BOTH', 'Both'),
    ]

    parameter = models.ForeignKey(
        Parameter,
        on_delete=models.CASCADE,
        related_name='reference_ranges'
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )

    machine_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    min_ref = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    max_ref = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    min_authz = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    max_authz = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    is_age_applicable = models.BooleanField(
        default=False
    )

    age_lower_limit = models.IntegerField(
        blank=True,
        null=True
    )

    age_upper_limit = models.IntegerField(
        blank=True,
        null=True
    )

    improbable_value_less = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    improbable_value_greater = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    is_reflex = models.BooleanField(
        default=False
    )

    reflex_value_less = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    reflex_value_greater = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    panic_value_less = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    panic_value_greater = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    varying_reference_range = models.TextField(
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    status = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "parameter_reference_ranges"
        ordering = ['-id']

    def __str__(self):
        return f"{self.parameter.parameter_name} - {self.gender}"