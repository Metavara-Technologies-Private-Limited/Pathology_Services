from django.db import models

class Clinic(models.Model):
    clinic_name = models.CharField(max_length=255)

    is_collection_location = models.BooleanField(default=False)
    is_processing_location = models.BooleanField(default=False)

    def __str__(self):
        return self.clinic_name
    
    class meta:
        db_table = "clinic"