from restapi.models.test_test import (
    TestTemplate
)


class TestTemplateLinkService:

    @staticmethod
    def get_all():

        return TestTemplate.objects.filter(
            is_deleted=False
        ).order_by('-id')

    @staticmethod
    def get_by_id(pk):

        try:

            return TestTemplate.objects.get(
                pk=pk,
                is_deleted=False
            )

        except TestTemplate.DoesNotExist:

            return None

    @staticmethod
    def create(validated_data):

        return TestTemplate.objects.create(
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