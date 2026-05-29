from rest_framework import serializers

from restapi.models.agency import Agency


class AgencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Agency
        fields = '__all__'