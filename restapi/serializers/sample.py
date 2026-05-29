from rest_framework import serializers
from restapi.models.sample import Sample

class SampleSerializer (serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'
