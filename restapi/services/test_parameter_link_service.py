from restapi.models.test_test import (
    TestParameter
)


class TestParameterLinkService:

    @staticmethod
    def get_all():

        return TestParameter.objects.filter(
            is_deleted=False
        ).order_by('display_order')

    @staticmethod
    def get_by_id(pk):

        try:

            return TestParameter.objects.get(
                pk=pk,
                is_deleted=False
            )

        except TestParameter.DoesNotExist:

            return None

    @staticmethod
    def create(validated_data):

        return TestParameter.objects.create(
            **validated_data
        )

    @staticmethod
    def update(instance, validated_data):

        for attr, value in validated_data.items():

            setattr(instance, attr, value)

        instance.save()

        return instance

    @staticmethod
    def delete(instance):

        instance.is_deleted = True

        instance.save()