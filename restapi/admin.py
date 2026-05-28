from django.contrib import admin

from .models import Patient,PendingShipment, ShipmentShipped, ShipmentReceived,ActivityLogs
admin.site.register(Patient)
admin.site.register(PendingShipment)
admin.site.register(ShipmentShipped)
admin.site.register(ShipmentReceived)
admin.site.register(ActivityLogs)

