from django.utils import timezone

from ..models import (
    Patient,
    PendingShipment,
    ShipmentShipped,
    ShipmentReceived,
    ActivityLogs
)


# =========================================
# PATIENT SERVICES
# =========================================

def create_patient(data):
    patient = Patient.objects.create(
        patient_name=data.get("patient_name"),
        age=data.get("age"),
        sex=data.get("sex"),
        mrn=data.get("mrn"),
        cycle_id=data.get("cycle_id")
    )
    return patient


def get_all_patients():
    return Patient.objects.all()


def get_patient_by_id(patient_id):
    return Patient.objects.get(id=patient_id)


# =========================================
# PENDING SHIPMENT SERVICES
# =========================================

def create_pending_shipment(data):
    patient = Patient.objects.get(id=data.get("patient"))

    pending = PendingShipment.objects.create(
        order_date=data.get("order_date"),
        sample_no=data.get("sample_no"),
        sample_type=data.get("sample_type"),
        test_code=data.get("test_code"),
        test_name=data.get("test_name"),
        service_name=data.get("service_name"),
        patient=patient
    )
    return pending


def get_all_pending_shipments():
    return PendingShipment.objects.all()


def get_pending_by_id(pending_id):
    return PendingShipment.objects.get(id=pending_id)



# =========================================
# ScheduleShipping
# =========================================


from restapi.models import (
    PendingShipment,
    ScheduleShipping
)


def create_schedule_shipping(data):

    pending = PendingShipment.objects.get(
        id=data.get("pending_id")
    )

    schedule = ScheduleShipping.objects.create(
        pending=pending,
        ship_date=data.get("ship_date"),
        ship_time=data.get("ship_time"),
        dispatched_by=data.get("dispatched_by"),
        ship_to=data.get("ship_to")
    )

    return schedule


def get_all_schedule_shipping():

    return ScheduleShipping.objects.all()


# =========================================
# MOVE PENDING → SHIPPED
# =========================================

def move_to_shipped(pending_id, ship_to, ship_by):
    pending = PendingShipment.objects.get(id=pending_id)

    shipped = ShipmentShipped.objects.create(
    ship_date=timezone.now(),
    shipment_no=f"SHIP-{pending.id}-{timezone.now().strftime('%H%M%S')}",
    pending_shipment=pending,
    ship_to=ship_to
)

    ActivityLogs.objects.create(
        shipped_shipment=shipped,
        ship_date_time=timezone.now(),
        ship_from="Main Lab",
        ship_to=ship_to,
        ship_by=ship_by
    )

    return shipped


def get_all_shipped_shipments():
    return ShipmentShipped.objects.all()


# =========================================
# MOVE SHIPPED → RECEIVED
# =========================================

def move_to_received(shipped_id, status_value, result_value):
    shipped = ShipmentShipped.objects.get(id=shipped_id)

    received = ShipmentReceived.objects.create(
        receive_date=timezone.now(),
        received_no=f"REC-{shipped.id}",
        shipped_shipment=shipped,
        status=status_value,
        result=result_value
    )

    return received


def get_all_received_shipments():
    return ShipmentReceived.objects.all()


# =========================================
# ACTIVITY LOGS SERVICES
# =========================================

def get_all_activity_logs():
    return ActivityLogs.objects.all()


def create_manual_activity_log(data):
    shipped = ShipmentShipped.objects.get(
        id=data.get("shipped_shipment")
    )

    log = ActivityLogs.objects.create(
        shipped_shipment=shipped,
        ship_date_time=timezone.now(),
        ship_from=data.get("ship_from"),
        ship_to=data.get("ship_to"),
        ship_by=data.get("ship_by")
    )

    return log