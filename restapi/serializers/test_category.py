from rest_framework import serializers
from restapi.models.test_category import Category
from restapi.models.test_test import Test
from restapi.services.test_category_service import CategoryService


class CategorySerializer(serializers.ModelSerializer):

    no_of_tests = serializers.SerializerMethodField()
    
    tests = serializers.SerializerMethodField()  # ← change to SerializerMethodField

    class Meta:
        model = Category
        fields = [
            'id',
            'category_code',
            'category_name',
            'status',
            'is_deleted',
            'created_at',
            'updated_at',
            'no_of_tests',
            'tests'
        ]

    def get_no_of_tests(self, obj):
        return obj.tests.count()

    def get_tests(self, obj):
     return [str(t.id) for t in obj.tests.all()]

    def create(self, validated_data):
        # tests comes from request data, not from get_tests
        tests_data = self.initial_data.get('tests', [])
        from restapi.models.test_test import Test
        tests = Test.objects.filter(id__in=tests_data)
        validated_data['tests'] = list(tests)
        return CategoryService.create_category(validated_data)

    def update(self, instance, validated_data):
        tests_data = self.initial_data.get('tests', [])
        from restapi.models.test_test import Test
        tests = Test.objects.filter(id__in=tests_data)
        validated_data['tests'] = list(tests)
        return CategoryService.update_category(instance, validated_data)