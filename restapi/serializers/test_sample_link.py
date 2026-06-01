from rest_framework import serializers

from restapi.models.test_test import (
    TestSample
)


class TestSampleLinkSerializer(
    serializers.ModelSerializer
):

    test_name = serializers.CharField(
        source='test.test_name',
        read_only=True
    )

    sample_name = serializers.CharField(
        source='sample.sample_name',
        read_only=True
    )

    sample_code = serializers.CharField(
        source='sample.sample_code',
        read_only=True
    )

    sample_code = serializers.CharField(
    source='sample.sample_code',
    read_only=True
    )

    class Meta:

        model = TestSample

        fields = "__all__"