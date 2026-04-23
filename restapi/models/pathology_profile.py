from django.db import models

class Pathology_profile(models.Model):
    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name="profiles")
    tests = models.ManyToManyField("Test")

    class Meta:
        db_table = "Pathology_profile"

    def __str__(self):
        return self.service_name