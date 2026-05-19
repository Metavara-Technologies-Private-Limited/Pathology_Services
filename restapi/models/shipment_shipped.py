from django.db import models
from .shipment_pending import PendingShipment

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
