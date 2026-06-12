from restapi.models.test_category import Category


class CategoryService:

    @staticmethod
    def create_category(validated_data):
        tests = validated_data.pop('tests', [])
        category = Category.objects.create(**validated_data)

        if tests:
            category.tests.set(tests)

        return category

    @staticmethod
    def update_category(instance, validated_data):
        tests = validated_data.pop('tests', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if tests is not None:
            instance.tests.set(tests)

        return instance