from rest_framework import serializers
from restapi.models.pathology_profile import Pathology_profile

class PathologyProfileSerializer(serializers.ModelSerializer):
    
    clinic_name = serializers.CharField(
    source="clinic.clinic_name",
    read_only=True
    )
    class Meta:
        model = Pathology_profile
        fields = '__all__'