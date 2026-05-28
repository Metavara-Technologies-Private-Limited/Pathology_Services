from django.db import models
from .shipment_pending import PendingShipment

class ScheduleShipping(models.Model):

    pending = models.ForeignKey(PendingShipment,on_delete=models.CASCADE)

    ship_date = models.DateField()

    ship_time = models.TimeField()

    dispatched_by = models.CharField(max_length=100)

    ship_to = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pending.sample_no} - {self.ship_to}"