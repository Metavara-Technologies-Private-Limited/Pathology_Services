from django.db import models
import uuid

from restapi.models.tube import Tube
from restapi.models.test_parameter import Parameter
from restapi.models.test_template import Template
from restapi.models.sample import Sample


class Test(models.Model):

    uuid = models.UUIDField(
    default=uuid.uuid4,
    editable=False,
    null=True,
    blank=True
   )

    REPORT_TYPE_CHOICES = [
        ('PARAMETER', 'By Parameter'),
        ('TEMPLATE', 'By Template'),
    ]

    test_code = models.CharField(
        max_length=50,
        unique=True
    )

    test_name = models.CharField(
        max_length=255
    )

    print_name = models.CharField(
        max_length=255
    )

    service_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    tube_name = models.ForeignKey(
        Tube,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tests'
    )

    test_completion_time = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    is_sensitive = models.BooleanField(
        default=False
    )

    suggestion_note = models.TextField(
        blank=True,
        null=True
    )

    disclaimer = models.TextField(
        blank=True,
        null=True
    )

    report_type = models.CharField(
        max_length=20,
        choices=REPORT_TYPE_CHOICES,
        default='PARAMETER'
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
        db_table = "tests"
        ordering = ['-id']

    def __str__(self):
        return self.test_name
    


class TestParameter(models.Model):

    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='test_parameters'
    )

    parameter = models.ForeignKey(
        Parameter,
        on_delete=models.CASCADE,
        related_name='parameter_tests'
    )

    display_order = models.PositiveIntegerField(
        default=1
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
        db_table = "test_parameters"
        ordering = ['display_order']

    def __str__(self):
        return f"{self.test.test_name} - {self.parameter.parameter_name}"
    


class TestTemplate(models.Model):

    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='test_templates'
    )

    template = models.ForeignKey(
        Template,
        on_delete=models.CASCADE,
        related_name='template_tests'
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
        db_table = "test_templates"
        ordering = ['-id']

    def __str__(self):
        return f"{self.test.test_name} - {self.template.template_name}"



class TestSample(models.Model):

    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='test_samples'
    )

    sample = models.ForeignKey(
        Sample,
        on_delete=models.CASCADE,
        related_name='sample_tests'
    )

    frequency = models.PositiveIntegerField(
        default=1
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
        db_table = "test_samples"
        ordering = ['-id']

    def __str__(self):
        return f"{self.test.test_name} - {self.sample.sample_name}"