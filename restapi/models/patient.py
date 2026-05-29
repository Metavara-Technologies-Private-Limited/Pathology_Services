from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()

    sex = models.CharField(max_length=10,choices=GENDER_CHOICES)

    mrn = models.CharField(max_length=100,unique=True,null=True,blank=True)

    cycle_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.patient_name} ({self.mrn})"

