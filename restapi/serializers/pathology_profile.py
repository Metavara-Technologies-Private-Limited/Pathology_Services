from rest_framework import serializers
from restapi.models.pathology_profile import Pathology_profile

class PathologyProfileSerializer(serializers.ModelSerializer):
    
    clinic_name = serializers.CharField(
        source="clinic.clinic_name",
        read_only=True
    )

    no_of_tests = serializers.SerializerMethodField()

    class Meta:
        model = Pathology_profile
        fields = '__all__'

    def get_no_of_tests(self, obj):
        return obj.tests.count()