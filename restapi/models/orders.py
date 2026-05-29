from django.db import models

# Create your views here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)

    PATIENT_TYPE = [
        ('walkin', 'Walk-in'),
        ('registered', 'Registered'),
    ]
    patient_type = models.CharField(max_length=20, choices=PATIENT_TYPE)

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class WorkOrder(models.Model):
    order_datetime = models.DateTimeField(auto_now_add=True)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    bill_number = models.CharField(max_length=50, primary_key=True)
    total_tests = models.PositiveIntegerField()

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('partial', 'Partial'),
        ('complete', 'Complete'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.bill_number