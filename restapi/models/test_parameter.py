from django.db import models
import uuid

class Parameter(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )


    TYPE_CHOICES = [
        ('NUMERIC', 'Numeric'),
        ('TEXT', 'Text'),
    ]

    UNIT_CHOICES = [
    ("mL", "mL"),
    ("mg/dL", "mg/dL"),
    ("cells/hpf", "cells/hpf"),
    ("%", "%"),
    ("IU/L", "IU/L"),
    ("NA", "NA"),
    ("IU/mL", "IU/mL"),
    ("meq/L", "meq/L"),
    ("mmol/L", "mmol/L"),
    ("ng/mL", "ng/mL"),
    ("g/dL", "g/dL"),
    ("pg", "pg"),
    ("ug/mL", "ug/mL"),
    ("mm in 1st hour", "mm in 1st hour"),
    ("pg/mL", "pg/mL"),
    ("pmol/dL", "pmol/dL"),
    ("pmol/L", "pmol/L"),
    ("nmol/L", "nmol/L"),
    ("umol/mL", "umol/mL"),
    ("x10^6 cells/cumm", "x10^6 cells/cumm"),
    ("U/L", "U/L"),
    ("x10^3 cells/cumm", "x10^3 cells/cumm"),
    ("uIU/mL", "uIU/mL"),
    ("umol/L", "umol/L"),
    ("x10^12/L", "x10^12/L"),
    ("x10^9/L", "x10^9/L"),
    ("fL", "fL"),
    ("sec", "sec"),
    ("mg/L", "mg/L"),
    ("mIU/mL", "mIU/mL"),
    ("ng/dL", "ng/dL"),
    ("mIU/L", "mIU/L"),
    ("ug/dL", "ug/dL"),
    ("Mil/mL", "Mil/mL"),
    ("mic/sec", "mic/sec"),
    ("Mil/ejac", "Mil/ejac"),
    ("min", "min"),
    ("Units", "Units"),
    ("Quality Score", "Quality Score"),
    ("Days", "Days"),
    ("Qualitative", "Qualitative"),
    ("cells/cumm.", "cells/cumm."),
    ("µg/mL", "µg/mL"),
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

    is_deleted = models.BooleanField(
        default=False
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

    is_deleted = models.BooleanField(
        default=False
    )

    class Meta:
        db_table = "parameter_reference_ranges"
        ordering = ['-id']

    def __str__(self):
        return f"{self.parameter.parameter_name} - {self.gender}"