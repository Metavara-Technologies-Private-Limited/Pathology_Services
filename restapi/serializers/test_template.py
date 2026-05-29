from rest_framework import serializers

from restapi.models.test_template import (
    Template,
    TemplateParameter
)


class TemplateParameterSerializer(serializers.ModelSerializer):

    parameter_name = serializers.CharField(
        source='parameter.parameter_name',
        read_only=True
    )

    class Meta:
        model = TemplateParameter
        fields = '__all__'


class TemplateSerializer(serializers.ModelSerializer):

    template_parameters = TemplateParameterSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Template
        fields = '__all__'