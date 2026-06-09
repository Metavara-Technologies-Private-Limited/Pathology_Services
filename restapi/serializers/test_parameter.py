from rest_framework import serializers
from restapi.models.test_parameter import (
    Parameter,
    ParameterReferenceRange
)

class ParameterReferenceRangeSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = ParameterReferenceRange
        fields = '__all__'
        extra_kwargs = {
            'parameter': {
                'required': False
            }
        }


class ParameterSerializer(serializers.ModelSerializer):

    reference_ranges = ParameterReferenceRangeSerializer(
        many=True,
        required=False
    )

    class Meta:
        model = Parameter
        fields = '__all__'


    def create(self, validated_data):

     reference_ranges_data = validated_data.pop(
        'reference_ranges',
        []
     )

     parameter = Parameter.objects.create(
        **validated_data
     )

     for ref_data in reference_ranges_data:

        ParameterReferenceRange.objects.create(
            parameter=parameter,
            **ref_data
        )

     return parameter


    def update(
    self,
    instance,
    validated_data
    ):

        reference_ranges_data = validated_data.pop(
        'reference_ranges',
        None
        )

        for attr, value in validated_data.items():

         setattr(
            instance,
            attr,
            value
            )

        instance.save()

        if reference_ranges_data is not None:

            instance.reference_ranges.all().delete()

            for ref_data in reference_ranges_data:

                ParameterReferenceRange.objects.create(
                parameter=instance,
                **ref_data
            )

        return instance