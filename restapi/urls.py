from django.urls import path
from .views import (
    PatientView,
    PendingShipmentView,
    MoveToShippedView,
    ShipmentShippedView,
    MoveToReceivedView,
    ShipmentReceivedView,
    ActivityLogsView
)

urlpatterns = [

    # Patient APIs
    path('patients/', PatientView.as_view(), name='patients'),

    # Pending Shipment APIs
    path('pending-shipment/', PendingShipmentView.as_view(), name='pending-shipment'),

    # Move Pending → Shipped
    path('move-to-shipped/', MoveToShippedView.as_view(), name='move-to-shipped'),

    # Shipped Shipment APIs
    path('shipped-shipment/', ShipmentShippedView.as_view(), name='shipped-shipment'),

    # Move Shipped → Received
    path('move-to-received/', MoveToReceivedView.as_view(), name='move-to-received'),

    # Received Shipment APIs
    path('received-shipment/', ShipmentReceivedView.as_view(), name='received-shipment'),

    # Activity Logs APIs
    path('activity-logs/', ActivityLogsView.as_view(), name='activity-logs'),
]