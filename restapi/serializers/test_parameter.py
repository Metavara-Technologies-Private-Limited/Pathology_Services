from rest_framework import serializers
from restapi.models.test_parameter import (
    Parameter,
    ParameterReferenceRange
)


class ParameterReferenceRangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParameterReferenceRange
        fields = '__all__'


class ParameterSerializer(serializers.ModelSerializer):

    reference_ranges = ParameterReferenceRangeSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Parameter
        fields = '__all__'