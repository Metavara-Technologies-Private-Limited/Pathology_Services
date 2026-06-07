from rest_framework import serializers

from restapi.models.test_category import Category


class CategorySerializer(serializers.ModelSerializer):

    no_of_tests = serializers.SerializerMethodField()

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
            'no_of_tests'
        ]

    def get_no_of_tests(self, obj):
        return obj.tests.count()