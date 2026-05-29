from restapi.models.test_test import (
    TestSample
)


class TestSampleLinkService:

    @staticmethod
    def get_all():

        return TestSample.objects.filter(
            is_deleted=False
        ).order_by('-id')

    @staticmethod
    def get_by_id(pk):

        try:

            return TestSample.objects.get(
                pk=pk,
                is_deleted=False
            )

        except TestSample.DoesNotExist:

            return None

    @staticmethod
    def create(validated_data):

        return TestSample.objects.create(
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