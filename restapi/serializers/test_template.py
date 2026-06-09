from rest_framework import serializers
from restapi.models.test_template import Template


class TemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Template
        fields = "__all__"