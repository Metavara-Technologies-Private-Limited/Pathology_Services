# from tkinter.filedialog import test

import attrs
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

        extra_kwargs = {
            'test': {'required': False}
        }


class TestTemplateSerializer(serializers.ModelSerializer):

    template_name = serializers.CharField(
        source='template.template_name',
        read_only=True
    )

    class Meta:
        model = TestTemplate
        fields = '__all__'

        extra_kwargs = {
        'test': {'required': False}
        }


class TestSampleSerializer(serializers.ModelSerializer):

    sample_name = serializers.CharField(
        source='sample.sample_name',
        read_only=True
    )

    class Meta:
       model = TestSample
       fields = '__all__'

       extra_kwargs = {
        'test': {'required': False}
    }

class TestSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
    source='category.category_name',
    read_only=True
)
    test_parameters = TestParameterSerializer(
        many=True,
        required=False
    )

    test_templates = TestTemplateSerializer(
        many=True,
        required=False
    )

    test_samples = TestSampleSerializer(
        many=True,
        required=False
    )

    tube_display_name = serializers.CharField(
        source='tube_name.tube_name',
        read_only=True
)

    class Meta:
        model = Test
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category_name'] = (
        instance.category.category_name
        if instance.category else None
    )
        return data


    def create(self, validated_data):

        test_parameters_data = validated_data.pop(
        'test_parameters',
        []
    )

        test_templates_data = validated_data.pop(
        'test_templates',
        []
    )

        test_samples_data = validated_data.pop(
        'test_samples',
        []
    )

        test = Test.objects.create(
        **validated_data
    )

        for param_data in test_parameters_data:

            TestParameter.objects.create(
            test=test,
            **param_data
        )

        for template_data in test_templates_data:

         TestTemplate.objects.create(
            test=test,
            **template_data
        )

        for sample_data in test_samples_data:

            TestSample.objects.create(
            test=test,
            **sample_data
        )

        return test
    

    def update(self, instance, validated_data):

        test_parameters_data = validated_data.pop(
        'test_parameters',
        None
    )

        test_templates_data = validated_data.pop(
        'test_templates',
        None
    )

        test_samples_data = validated_data.pop(
        'test_samples',
        None
    )

        for attr, value in validated_data.items():

            setattr(
            instance,
            attr,
            value
        )

        instance.save()

        if test_parameters_data is not None:

            instance.test_parameters.all().delete()

            for param_data in test_parameters_data:

                TestParameter.objects.create(
                test=instance,
                **param_data
            )

        if test_templates_data is not None:

            instance.test_templates.all().delete()

            for template_data in test_templates_data:

                TestTemplate.objects.create(
                test=instance,
                **template_data
            )

        if test_samples_data is not None:

            instance.test_samples.all().delete()

            for sample_data in test_samples_data:

                TestSample.objects.create(
                test=instance,
                **sample_data
            )

        return instance
    

    def validate(self, attrs):

        report_type = attrs.get('report_type')

        test_parameters = attrs.get(
        'test_parameters',
        []
    )

        test_templates = attrs.get(
        'test_templates',
        []
    )

        if (report_type == 'PARAMETER' and test_templates):

            raise serializers.ValidationError(
            {
                "test_templates":
                "Not allowed when report type is PARAMETER."
            }
        )

        if (report_type == 'TEMPLATE' and test_parameters):

            raise serializers.ValidationError(
            {
                "test_parameters":
                "Not allowed when report type is TEMPLATE."
            }
        )

        return attrs