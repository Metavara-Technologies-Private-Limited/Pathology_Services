from django.db import models
from restapi.models.test_parameter import Parameter
import uuid

class Template(models.Model):

    uuid = models.UUIDField(
    default=uuid.uuid4,
    editable=False,
    null=True,
    blank=True
    )

    TEMPLATE_FOR_CHOICES = [
        ('TEST', 'Test'),
        ('PROFILE', 'Profile'),
    ]

    TEMPLATE_TYPE_CHOICES = [
        ('TEXT', 'Text'),
        ('TABLE', 'Table'),
    ]

    template_code = models.CharField(
        max_length=50,
        unique=True
    )

    template_name = models.CharField(
        max_length=255
    )

    template_for = models.CharField(
        max_length=20,
        choices=TEMPLATE_FOR_CHOICES
    )

    template_type = models.CharField(
        max_length=20,
        choices=TEMPLATE_TYPE_CHOICES
    )

    template_text = models.TextField(
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
        ordering = ['-id']

    def __str__(self):
        return self.template_name


class TemplateParameter(models.Model):

    template = models.ForeignKey(
        Template,
        on_delete=models.CASCADE,
        related_name='template_parameters'
    )

    parameter = models.ForeignKey(
        Parameter,
        on_delete=models.CASCADE,
        related_name='parameter_templates'
    )

    display_order = models.PositiveIntegerField(
        default=1
    )

    is_required = models.BooleanField(
        default=True
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
        db_table = "template_parameters"
        ordering = ['display_order']

    def __str__(self):
        return f"{self.template.template_name} - {self.parameter.parameter_name}"