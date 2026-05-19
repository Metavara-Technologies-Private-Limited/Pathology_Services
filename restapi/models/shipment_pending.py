from django.db import models
from .patient import Patient

class PendingShipment(models.Model):
    
    order_date = models.DateTimeField()

    sample_no = models.CharField(max_length=100, unique=True,null=True,
    blank=True)
    SAMPLE_TYPE_CHOICES = [
        ('Blood', 'Blood'),
        ('Urine', 'Urine'),
    ]
    sample_type = models.CharField(max_length=50,choices=SAMPLE_TYPE_CHOICES,default="Blood")
    
    test_code = models.CharField(max_length=100)
    test_name = models.CharField(max_length=100)

    service_name = models.CharField(max_length=200)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True,
    blank=True,related_name='pending_shipments')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sample_no
