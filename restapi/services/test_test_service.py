from restapi.models.test_test import (
    Test,
    TestParameter,
    TestTemplate,
    TestSample
)


class TestService:

    @staticmethod
    def get_all_tests():
        return Test.objects.filter(
            is_deleted=False
        ).order_by('-id')

    @staticmethod
    def get_test_by_id(test_id):
        return Test.objects.filter(
            id=test_id,
            is_deleted=False
        ).first()

    @staticmethod
    def create_test(validated_data):
        return Test.objects.create(**validated_data)

    @staticmethod
    def update_test(instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

    @staticmethod
    def delete_test(instance):

        instance.is_deleted = True
        instance.save()

        return True