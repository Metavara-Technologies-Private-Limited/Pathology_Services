# PendingShipment
from django.db import models

from restapi.models.collection import Collection
from .patient import Patient

class PendingShipment(models.Model):
#Updated upstream

#Stashed changes

#Stashed changes
    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending')
    ]

#Updated upstream
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

 #Stashed changes
    scheduled_collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    order_date = models.DateTimeField()

    sample_no = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True
    )

    SAMPLE_TYPE_CHOICES = [
        ('Blood', 'Blood'),
        ('Urine', 'Urine'),
    ]

    sample_type = models.CharField(
        max_length=50,
        choices=SAMPLE_TYPE_CHOICES,
        default="Blood"
    )

    test_code = models.CharField(max_length=100)

    test_name = models.CharField(max_length=100)

    service_name = models.CharField(max_length=200)

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='pending_shipments'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"Pending Shipment {self.id} - {self.status}"

#  ScheduleShipping
from .shipment import PendingShipment

class ScheduleShipping(models.Model):

    pending = models.ForeignKey(PendingShipment,on_delete=models.CASCADE)

    ship_date = models.DateField()

    ship_time = models.TimeField()

    dispatched_by = models.CharField(max_length=100)

    ship_to = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pending.sample_no} - {self.ship_to}"



#  ShipmentShipped
from .shipment import PendingShipment

class ShipmentShipped(models.Model):
    ship_date = models.DateTimeField()

    shipment_no = models.CharField(
        max_length=100,
        unique=True
    )

    pending_shipment = models.ForeignKey(
        PendingShipment,
        on_delete=models.CASCADE, null=True,
        blank=True,
        related_name='shipped_records',
        
    )

    ship_to = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shipment_no
    

#  ShipmentReceived
from .shipment import ShipmentShipped

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
 

 # ActivityLogs
from .shipment import ShipmentShipped

class ActivityLogs(models.Model):
    shipped_shipment = models.ForeignKey( ShipmentShipped,
        on_delete=models.CASCADE,null=True,blank=True,
        related_name='activity_logs'
    )

    ship_date_time = models.DateTimeField()

    ship_from = models.CharField(max_length=100)

    ship_to = models.CharField(max_length=100)

    ship_by = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shipped_shipment.shipment_no

