from django.db import models
import uuid

class Category(models.Model):

    uuid = models.UUIDField(
    default=uuid.uuid4,
    editable=False,
    unique=True
    )

    tests = models.ManyToManyField(
        'Test',
        related_name='categories',
        blank=True
    )

    category_code = models.CharField(
        max_length=50,
        unique=True
    )

    category_name = models.CharField(
        max_length=100
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
        db_table = "categories"
        ordering = ['-id']

    def __str__(self):
        return self.category_name