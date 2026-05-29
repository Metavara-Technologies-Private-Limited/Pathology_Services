from restapi.models import (
    Parameter,
    ParameterReferenceRange
)


def get_all_parameters():
    return Parameter.objects.all()


def get_parameter_by_id(parameter_id):
    return Parameter.objects.get(id=parameter_id)


def get_all_reference_ranges():
    return ParameterReferenceRange.objects.all()


def get_reference_range_by_id(reference_range_id):
    return ParameterReferenceRange.objects.get(
        id=reference_range_id
    )