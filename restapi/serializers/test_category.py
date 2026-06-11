from rest_framework import serializers
from restapi.models.test_category import Category
from restapi.models.test_test import Test
from restapi.services.test_category_service import CategoryService


class CategorySerializer(serializers.ModelSerializer):

    no_of_tests = serializers.SerializerMethodField()
    
    tests = serializers.PrimaryKeyRelatedField(
        queryset=Test.objects.all(),
        many=True,
        write_only=True,
        required=False
)
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
    
    def create(self, validated_data):
        return CategoryService.create_category(
        validated_data
    )

    def update(self, instance, validated_data):
        return CategoryService.update_category(
        instance,
        validated_data
    )