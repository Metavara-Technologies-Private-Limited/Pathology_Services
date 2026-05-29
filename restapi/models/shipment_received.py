from django.db import models
from .shipment_shipped import ShipmentShipped

class ShipmentReceived(models.Model):
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    receive_date = models.DateTimeField()

    received_no = models.CharField(max_length=100,unique=True)

    shipped_shipment = models.ForeignKey(ShipmentShipped,on_delete=models.CASCADE,
         null=True,blank=True,related_name='received_records'
    )

    status = models.CharField(max_length=50,choices=STATUS_CHOICES)

    result = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.received_no
