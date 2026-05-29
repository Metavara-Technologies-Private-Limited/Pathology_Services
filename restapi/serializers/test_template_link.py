from rest_framework import serializers

from restapi.models.test_test import (
    TestTemplate
)


class TestTemplateLinkSerializer(
    serializers.ModelSerializer
):

    test_name = serializers.CharField(
        source='test.test_name',
        read_only=True
    )

    template_name = serializers.CharField(
        source='template.template_name',
        read_only=True
    )

    class Meta:

        model = TestTemplate

        fields = "__all__"