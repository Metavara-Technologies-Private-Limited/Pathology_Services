from rest_framework import serializers

from restapi.models.test_test import (
    TestParameter
)


class TestParameterLinkSerializer(
    serializers.ModelSerializer
):

    test_name = serializers.CharField(
        source='test.test_name',
        read_only=True
    )

    parameter_name = serializers.CharField(
        source='parameter.parameter_name',
        read_only=True
    )

    class Meta:

        model = TestParameter

        fields = "__all__"