from restapi.models.test_category import Category
from restapi.models.test_test import Test


class CategoryService:

    @staticmethod
    def create_category(validated_data):

        tests = validated_data.pop('tests', [])

        category = Category.objects.create(
            **validated_data
        )

        for test in tests:
            test.category = category
            test.save()

        return category

    @staticmethod
    def update_category(instance, validated_data):

        tests = validated_data.pop('tests', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if tests is not None:

            Test.objects.filter(
                category=instance
            ).update(
                category=None
            )

            for test in tests:
                test.category = instance
                test.save()

        return instance