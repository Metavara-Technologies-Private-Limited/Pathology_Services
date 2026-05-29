from rest_framework import serializers

from restapi.models.test_test import Test
from restapi.models.test_test import (
    Test,
    TestParameter,
    TestTemplate,
    TestSample
)

class TestParameterSerializer(serializers.ModelSerializer):

    parameter_name = serializers.CharField(
        source='parameter.parameter_name',
        read_only=True
    )

    class Meta:
        model = TestParameter
        fields = '__all__'


class TestTemplateSerializer(serializers.ModelSerializer):

    template_name = serializers.CharField(
        source='template.template_name',
        read_only=True
    )

    class Meta:
        model = TestTemplate
        fields = '__all__'


class TestSampleSerializer(serializers.ModelSerializer):

    sample_name = serializers.CharField(
        source='sample.sample_name',
        read_only=True
    )

    class Meta:
        model = TestSample
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):

    test_parameters = TestParameterSerializer(
        many=True,
        read_only=True
    )

    test_templates = TestTemplateSerializer(
        many=True,
        read_only=True
    )

    test_samples = TestSampleSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Test
        fields = '__all__'