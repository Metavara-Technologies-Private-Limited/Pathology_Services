from restapi.models.collection import Collection


def get_collections(
    *,
    work_order_id=None,
    patient_id=None,
    test_type=None,
    status=None,
    agency_id=None,
    date_from=None,
    date_to=None,
):
    queryset = Collection.objects.select_related(
        "test",
        "sample",
        "agency",
    )

    if work_order_id:
        queryset = queryset.filter(
            work_order_id=work_order_id
        )

    if patient_id:
        queryset = queryset.filter(
            patient_id=patient_id
        )

    if test_type:
        queryset = queryset.filter(
            test_type=test_type
        )

    if status:
        queryset = queryset.filter(
            status=status
        )

    if agency_id:
        queryset = queryset.filter(
            agency_id=agency_id
        )

    if date_from:
        queryset = queryset.filter(
            collection_date__gte=date_from
        )

    if date_to:
        queryset = queryset.filter(
            collection_date__lte=date_to
        )

    return queryset


def get_collection_by_id(
    collection_id,
) -> Collection:
    return (
        Collection.objects
        .select_related(
            "test",
            "sample",
            "agency",
        )
        .get(id=collection_id)
    )