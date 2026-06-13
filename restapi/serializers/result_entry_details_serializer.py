from rest_framework import serializers


class ParameterDetailsSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    parameter_name = serializers.CharField()
    parameter_code = serializers.CharField()
    unit = serializers.CharField()

    min_ref = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)

    max_ref = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)

    min_authz = serializers.DecimalField(
        max_digits=10, decimal_places=2, allow_null=True
    )

    max_authz = serializers.DecimalField(
        max_digits=10, decimal_places=2, allow_null=True
    )

    varying_reference_range = serializers.CharField(allow_null=True)
