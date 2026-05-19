from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services.services import (
    create_patient,
    get_all_patients,
    get_patient_by_id,
    create_pending_shipment,
    get_all_pending_shipments,
    get_pending_by_id,
    move_to_shipped,
    get_all_shipped_shipments,
    move_to_received,
    get_all_received_shipments,
    get_all_activity_logs,
    create_manual_activity_log
)


# =========================================
# PATIENT VIEWS
# =========================================

class PatientView(APIView):

    def get(self, request):
        patients = get_all_patients()

        data = []
        for patient in patients:
            data.append({
                "id": patient.id,
                "patient_name": patient.patient_name,
                "age": patient.age,
                "sex": patient.sex,
                "mrn": patient.mrn,
                "cycle_id": patient.cycle_id
            })

        return Response(data)

    def post(self, request):
        patient = create_patient(request.data)

        return Response({
            "message": "Patient created successfully",
            "id": patient.id
        }, status=status.HTTP_201_CREATED)


# =========================================
# PENDING SHIPMENT VIEWS
# =========================================

class PendingShipmentView(APIView):

    def get(self, request):
        pendings = get_all_pending_shipments()

        data = []
        for item in pendings:
            data.append({
                "id": item.id,
                "sample_no": item.sample_no,
                "sample_type": item.sample_type,
                "test_code": item.test_code,
                "test_name": item.test_name,
                "service_name": item.service_name,
                "patient": item.patient.patient_name
            })

        return Response(data)

    def post(self, request):
        pending = create_pending_shipment(request.data)

        return Response({
            "message": "Pending Shipment created successfully",
            "id": pending.id
        }, status=status.HTTP_201_CREATED)


# =========================================
# MOVE TO SHIPPED VIEW
# =========================================

class MoveToShippedView(APIView):

    def post(self, request):
        pending_id = request.data.get("pending_id")
        ship_to = request.data.get("ship_to")
        ship_by = request.data.get("ship_by")

        shipped = move_to_shipped(
            pending_id,
            ship_to,
            ship_by
        )

        return Response({
            "message": "Shipment moved to shipped successfully",
            "shipment_no": shipped.shipment_no
        }, status=status.HTTP_201_CREATED)


# =========================================
# SHIPPED SHIPMENT VIEW
# =========================================

class ShipmentShippedView(APIView):

    def get(self, request):
        shipments = get_all_shipped_shipments()

        data = []
        for item in shipments:
            data.append({
                "id": item.id,
                "shipment_no": item.shipment_no,
                "ship_date": item.ship_date,
                "sample_no": item.pending_shipment.sample_no,
                "patient": item.pending_shipment.patient.patient_name,
                "ship_to": item.ship_to
            })

        return Response(data)


# =========================================
# MOVE TO RECEIVED VIEW
# =========================================

class MoveToReceivedView(APIView):

    def post(self, request):
        shipped_id = request.data.get("shipped_id")
        status_value = request.data.get("status")
        result_value = request.data.get("result")

        received = move_to_received(
            shipped_id,
            status_value,
            result_value
        )

        return Response({
            "message": "Shipment moved to received successfully",
            "received_no": received.received_no
        }, status=status.HTTP_201_CREATED)


# =========================================
# RECEIVED SHIPMENT VIEW
# =========================================

class ShipmentReceivedView(APIView):

    def get(self, request):
        receiveds = get_all_received_shipments()

        data = []
        for item in receiveds:
            data.append({
                "id": item.id,
                "received_no": item.received_no,
                "receive_date": item.receive_date,
                "shipment_no": item.shipped_shipment.shipment_no,
                "status": item.status,
                "result": item.result
            })

        return Response(data)


# =========================================
# ACTIVITY LOGS VIEW
# =========================================

class ActivityLogsView(APIView):
    def get(self, request):
        logs = get_all_activity_logs()

        data = []

        for log in logs:
            data.append({
                "id": log.id,
                "ship_no": log.shipped_shipment.shipment_no if log.shipped_shipment else None,
                "ship_from": log.ship_from,
                "ship_to": log.ship_to,
                "ship_by": log.ship_by,
                "ship_date_time": log.ship_date_time,
            })

        return Response(data)