from django.db import models
from .pathology_profile import Pathology_profile

class Template(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    template_code = models.CharField(max_length=50, unique=True)
    template_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    pathologist =models.ForeignKey(Pathology_profile, on_delete=models.CASCADE, related_name="template")
    template_format = models.TextField()

    def __str__(self):
        return self.template_name