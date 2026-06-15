import uuid

import requests
from django.conf import settings
from django.db import transaction
from django.utils import timezone

from restapi.constants.order_status import (
    TestStatus,
    TestType,
)
from restapi.models.agency import Agency
from restapi.models.collection import Collection
from restapi.workflows.order_workflow import (
    transition_test_status,
)


def get_vidai_access_token() -> str:
    response = requests.post(
        settings.EXTERNAL_LOGIN_URL,
        json={
            "username": settings.EXTERNAL_USERNAME,
            "password": settings.EXTERNAL_PASSWORD,
            "force_login": True,
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()["access"]


def fetch_vidai_orders(
    limit=10,
    offset=0,
    search=None,
    from_date=None,
    to_date=None,
) -> dict:
    token = get_vidai_access_token()

    params = {
        "limit": limit,
        "offset": offset,
    }
    if search:
        params["search"] = search
    if from_date:
        params["from_date"] = from_date
    if to_date:
        params["to_date"] = to_date

    response = requests.get(
        settings.ORDERS_URL,
        params=params,
        headers={
            "Authorization": f"Bearer {token}"
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def fetch_vidai_order_detail(order_id: int) -> dict:
    token = get_vidai_access_token()

    url = f"{settings.ORDERS_URL}{order_id}/"

    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {token}"
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()

def get_invoice_item(
    order_data: dict,
    invoice_item_id: int = None,
    test_service_id: int = None,
) -> dict:
    for item in order_data.get("invoice_items", []):
        if invoice_item_id and item.get("id") == invoice_item_id:
            return item
        if test_service_id and item.get("test_service_id") == test_service_id:
            return item

    raise ValueError(
        f"No invoice item found for "
        f"invoice_item_id={invoice_item_id} "
        f"or test_service_id={test_service_id}"
    )
def resolve_test_from_service_id(service_id: int):
    from restapi.models.test_test import Test
    try:
        return Test.objects.get(
            test_service_id=service_id
        )
    except Test.DoesNotExist:
        return None


def _build_identifier(prefix: str) -> str:
    date_part = timezone.now().strftime("%Y%m%d")
    random_part = uuid.uuid4().hex[:8].upper()
    return f"{prefix}{date_part}{random_part}"


def generate_collection_identifiers() -> dict:
    while True:
        barcode_value = _build_identifier("BC")
        specimen_no = _build_identifier("SP")

        exists = (
            Collection.objects.filter(
                barcode_value=barcode_value
            ).exists()
            or
            Collection.objects.filter(
                specimen_no=specimen_no
            ).exists()
        )

        if not exists:
            return {
                "barcode_value": barcode_value,
                "specimen_no": specimen_no,
            }


@transaction.atomic
def create_collection(**validated_data) -> Collection:

    identifiers = generate_collection_identifiers()

    work_order_id = validated_data.get("work_order_id")
    test_service_id = validated_data.get("test_service_id")

    if not work_order_id:
        raise ValueError("work_order_id is required")

    if not test_service_id:
        raise ValueError("test_service_id is required")
    
    invoice_item_id = validated_data.get("invoice_item_id")

    # Duplicate protection
    existing = Collection.objects.filter(
        work_order_id=work_order_id,
        invoice_item_id=invoice_item_id,
    ).first() if invoice_item_id else None

    if existing:
        return existing

    # -----------------------------------
    # Fetch full order details from Vidai
    # -----------------------------------

    order_data = fetch_vidai_order_detail(work_order_id)

    patient = order_data.get("patient", {})

    invoice_item = get_invoice_item(
        order_data,
        invoice_item_id=validated_data.get("invoice_item_id"),
        test_service_id=test_service_id,
    )

    # -----------------------------------
    # Order-level fields
    # -----------------------------------

    validated_data["bill_number"] = order_data.get("bill_number")
    validated_data["bill_type"] = order_data.get("bill_type")
    validated_data["visit_id"] = order_data.get("visit_id")
    validated_data["visit_date"] = order_data.get("visit_date")

    # -----------------------------------
    # Patient-level fields
    # -----------------------------------

    validated_data["patient_name"] = patient.get("name")
    validated_data["patient_mrn"] = patient.get("mrn")
    validated_data["patient_age"] = patient.get("age")
    validated_data["patient_gender"] = patient.get("gender")
    validated_data["patient_type"] = patient.get("patient_type")
    validated_data["cycle_number"] = patient.get("cycle_number")

    first_name = patient.get("doctor_first_name", "") or ""
    last_name = patient.get("doctor_last_name", "") or ""

    validated_data["doctor_name"] = (
        f"{first_name} {last_name}"
    ).strip()

    # -----------------------------------
    # Invoice-item fields
    # -----------------------------------

    validated_data["invoice_item_id"] = invoice_item.get("id")

    validated_data["billing_source_type"] = (
        invoice_item.get("billing_source_type")
    )

    validated_data["billing_source_id"] = (
        invoice_item.get("billing_source_id")
    )

    validated_data["billing_source_code"] = (
        invoice_item.get("billing_source_code")
    )

    validated_data["billing_source_name"] = (
        invoice_item.get("billing_source_name")
    )

    validated_data["test_service_code"] = (
        invoice_item.get("test_service_code")
    )

    validated_data["test_service_name"] = (
        invoice_item.get("test_service_name")
    )

    validated_data["charges"] = (
        invoice_item.get("charges")
    )

    validated_data["net_amount"] = (
        invoice_item.get("net_amount")
    )

    validated_data["is_from_package"] = (
        invoice_item.get("is_from_package", False)
    )

    validated_data["is_refunded"] = (
        invoice_item.get("is_refunded", False)
    )

    # -----------------------------------
    # Resolve local test
    # -----------------------------------

    if validated_data.get("test") is None:

        test = resolve_test_from_service_id(
            validated_data["test_service_id"]
        )

        if test:
            validated_data["test"] = test

            # Auto-resolve sample from test master
            if validated_data.get("sample") is None:
                test_sample = test.test_samples.filter(
                    is_deleted=False
                ).first()
                if test_sample:
                    validated_data["sample"] = test_sample.sample

    # -----------------------------------
    # Create collection
    # -----------------------------------

    collection = Collection.objects.create(
        **validated_data,
        status=TestStatus.COLLECTED,
        barcode_value=identifiers["barcode_value"],
        specimen_no=identifiers["specimen_no"],
    )

    return collection


@transaction.atomic
def update_collection_status(
    collection_id,
    new_status: str,
) -> Collection:

    collection = (
        Collection.objects
        .select_for_update()
        .get(id=collection_id)
    )

    transition_test_status(
        collection.status,
        new_status,
    )

    collection.status = new_status

    collection.save(
        update_fields=[
            "status",
            "updated_at",
        ]
    )

    return collection


@transaction.atomic
def change_collection_agency(
    *,
    collection_id,
    new_agency_id,
    reason: str,
) -> Collection:

    collection = (
        Collection.objects
        .select_for_update()
        .get(id=collection_id)
    )

    if collection.test_type != TestType.OUTSOURCE:
        raise ValueError(
            "Agency can only be changed "
            "for outsourced collections."
        )

    if collection.status not in (
        TestStatus.COLLECTED,
        TestStatus.SHIPPED,
    ):
        raise ValueError(
            "Agency can only be changed "
            "before sample is received."
        )

    agency = Agency.objects.get(id=new_agency_id)

    collection.agency = agency
    collection.agency_change_reason = reason

    collection.save(
        update_fields=[
            "agency",
            "agency_change_reason",
            "updated_at",
        ]
    )

    return collection
