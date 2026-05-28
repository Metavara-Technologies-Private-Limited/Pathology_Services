from django.db import models
from .shipment_shipped import ShipmentShipped

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