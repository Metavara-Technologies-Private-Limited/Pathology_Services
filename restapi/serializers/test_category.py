from rest_framework import serializers

from restapi.models.test_category import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'