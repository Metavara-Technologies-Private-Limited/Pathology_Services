from django.shortcuts import render, get_object_or_404 
from restapi.models.sample import Sample        
from rest_framework import viewsets, status
from rest_framework.response import Response
from restapi.serializers.sample import SampleSerializer
from restapi.services import sample_service
from rest_framework.viewsets import ViewSet
from restapi.models import Tube
from restapi.serializers.tube import TubeSerializer
from restapi.services import tube_service
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from restapi.serializers.agency import AgencySerializer
from restapi.services.agency_service import AgencyService
from rest_framework.viewsets import ModelViewSet
from restapi.serializers.machine import MachineSerializer
from restapi.services.machine_service import MachineService
from restapi.serializers.pathology_profile import (
    PathologyProfileSerializer
)
from restapi.services.pathology_profile_service import (
    PathologyProfileService
)
from restapi.models.test_category import Category
from restapi.serializers.test_category import CategorySerializer

from restapi.models.test_template import (
    Template,
    TemplateParameter
)
from restapi.serializers.test_template import (
    TemplateSerializer,
    TemplateParameterSerializer
)
from restapi.services.test_template_service import (
    TemplateService,
    TemplateParameterService
)

# ==================================
# Tube_(Master)_ViewSet
# ==================================

class SampleViewSet(viewsets.ViewSet):

    def list(self, request):
        samples = sample_service.get_all_samples()
        serializer = SampleSerializer(samples, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            sample = sample_service.create_sample(serializer.validated_data)
            return Response(SampleSerializer(sample).data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        sample = get_object_or_404(Sample, id=pk)
        serializer = SampleSerializer(sample)
        return Response(serializer.data)

    def update(self, request, pk=None):
        sample = sample_service.get_sample(pk)
        serializer = SampleSerializer(sample, data=request.data)
        if serializer.is_valid():
            updated = sample_service.update_sample(sample, serializer.validated_data)
            return Response(SampleSerializer(updated).data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        sample = sample_service.get_sample(pk)
        sample_service.delete_sample(sample)
        return Response(status=204)
    
# ==================================
# Tube_(Master)_ViewSet
# ==================================

class TubeViewSet(ViewSet):

    def list(self, request):
        tubes = tube_service.get_all_tubes()
        serializer = TubeSerializer(tubes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tube = get_object_or_404(Tube, pk=pk)
        serializer = TubeSerializer(tube)
        return Response(serializer.data)

    def create(self, request):
        serializer = TubeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        tube = get_object_or_404(Tube, pk=pk)
        serializer = TubeSerializer(tube, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        tube = get_object_or_404(Tube, pk=pk)
        tube.delete()
        return Response(status=204)
    

#--------------------------------------------------------

from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from restapi.models import (
    Parameter,
    ParameterReferenceRange
)

from restapi.serializers.test_parameter import (
    ParameterSerializer,
    ParameterReferenceRangeSerializer
)

from restapi.services import test_parameter_service

# ==================================
# Parameter_(Master)_ViewSet
# ==================================

from restapi.services import test_parameter_service

class ParameterViewSet(viewsets.ViewSet):

    def list(self, request):

        parameters = (
            test_parameter_service.get_all_parameters()
        )

        serializer = ParameterSerializer(
            parameters,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        parameter = get_object_or_404(
            Parameter,
            pk=pk
        )

        serializer = ParameterSerializer(parameter)

        return Response(serializer.data)

    def create(self, request):

        serializer = ParameterSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )

    def update(self, request, pk=None):

        parameter = get_object_or_404(
            Parameter,
            pk=pk
        )

        serializer = ParameterSerializer(
            parameter,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=400
        )

    def destroy(self, request, pk=None):

        parameter = get_object_or_404(
            Parameter,
            pk=pk
        )

        parameter.delete()

        return Response(status=204)


# ==================================
# Parameter_ReferenceRange_ViewSet
# ==================================

class ParameterReferenceRangeViewSet(viewsets.ViewSet):

    def list(self, request):

        reference_ranges = (
            test_parameter_service.get_all_reference_ranges()
        )

        serializer = (
            ParameterReferenceRangeSerializer(
                reference_ranges,
                many=True
            )
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        reference_range = get_object_or_404(
            ParameterReferenceRange,
            pk=pk
        )

        serializer = (
            ParameterReferenceRangeSerializer(
                reference_range
            )
        )

        return Response(serializer.data)

    def create(self, request):

        serializer = (
            ParameterReferenceRangeSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )

    def update(self, request, pk=None):

        reference_range = get_object_or_404(
            ParameterReferenceRange,
            pk=pk
        )

        serializer = (
            ParameterReferenceRangeSerializer(
                reference_range,
                data=request.data
            )
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=400
        )

    def destroy(self, request, pk=None):

        reference_range = get_object_or_404(
            ParameterReferenceRange,
            pk=pk
        )

        reference_range.delete()

        return Response(status=204)
    

# ==================================
# Template_Master_ViewSet
# ==================================

class TemplateViewSet(ViewSet):

    def list(self, request):

        queryset = TemplateService.get_all()
        serializer = TemplateSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = TemplateService.get_by_id(pk)

        if not instance:
            return Response(
                {"error": "Template not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TemplateSerializer(instance)

        return Response(serializer.data)

    def create(self, request):

        serializer = TemplateSerializer(data=request.data)

        if serializer.is_valid():

            instance = TemplateService.create(
                serializer.validated_data
            )

            response_serializer = TemplateSerializer(instance)

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = TemplateService.get_by_id(pk)

        if not instance:
            return Response(
                {"error": "Template not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TemplateSerializer(
            instance,
            data=request.data
        )

        if serializer.is_valid():

            updated_instance = TemplateService.update(
                instance,
                serializer.validated_data
            )

            response_serializer = TemplateSerializer(updated_instance)

            return Response(response_serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = TemplateService.get_by_id(pk)

        if not instance:
            return Response(
                {"error": "Template not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        TemplateService.soft_delete(instance)

        return Response(
            {"message": "Template deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

# ==================================
# Template_Parameter_ViewSet
# ==================================

class TemplateParameterViewSet(ViewSet):

    def list(self, request):

        queryset = TemplateParameterService.get_all()

        serializer = TemplateParameterSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = TemplateParameterService.get_by_id(pk)

        if not instance:
            return Response(
                {"error": "Template Parameter not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TemplateParameterSerializer(instance)

        return Response(serializer.data)

    def create(self, request):

        serializer = TemplateParameterSerializer(
            data=request.data
        )

        if serializer.is_valid():

            instance = TemplateParameterService.create(
                serializer.validated_data
            )

            response_serializer = TemplateParameterSerializer(
                instance
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = TemplateParameterService.get_by_id(pk)

        if not instance:
            return Response(
                {"error": "Template Parameter not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TemplateParameterSerializer(
            instance,
            data=request.data
        )

        if serializer.is_valid():

            updated_instance = TemplateParameterService.update(
                instance,
                serializer.validated_data
            )

            response_serializer = TemplateParameterSerializer(
                updated_instance
            )

            return Response(response_serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = TemplateParameterService.get_by_id(pk)

        if not instance:
            return Response(
                {"error": "Template Parameter not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        TemplateParameterService.soft_delete(instance)

        return Response(
            {"message": "Template Parameter deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
    

# ==================================
# Test_ViewSet
# ==================================
    
from restapi.serializers.test_test import TestSerializer
from restapi.services.test_test_service import TestService

class TestViewSet(ViewSet):

    def list(self, request):

        queryset = TestService.get_all_tests()

        serializer = TestSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = TestService.get_test_by_id(pk)

        if not instance:
            return Response(
                {"error": "Test not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TestSerializer(instance)

        return Response(serializer.data)

    def create(self, request):

        serializer = TestSerializer(
            data=request.data
        )

        if serializer.is_valid():

            instance = TestService.create_test(
                serializer.validated_data
            )

            response_serializer = TestSerializer(instance)

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = TestService.get_test_by_id(pk)

        if not instance:
            return Response(
                {"error": "Test not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TestSerializer(
            instance,
            data=request.data
        )

        if serializer.is_valid():

            updated_instance = TestService.update_test(
                instance,
                serializer.validated_data
            )

            response_serializer = TestSerializer(
                updated_instance
            )

            return Response(response_serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = TestService.get_test_by_id(pk)

        if not instance:
            return Response(
                {"error": "Test not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        TestService.delete_test(instance)

        return Response(
            {"message": "Test deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
    
class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all().order_by('-id')

    serializer_class = CategorySerializer


# ==================================
# Profile_Master_ViewSet
# ==================================

class PathologyProfileViewSet(ViewSet):

    def list(self, request):

        queryset = PathologyProfileService.get_all_profiles()

        serializer = PathologyProfileSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = PathologyProfileService.get_profile_by_id(pk)

        if not instance:
            return Response(
                {"error": "Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PathologyProfileSerializer(instance)

        return Response(serializer.data)

    def create(self, request):

        serializer = PathologyProfileSerializer(
            data=request.data
        )

        if serializer.is_valid():

            instance = PathologyProfileService.create_profile(
                serializer.validated_data
            )

            response_serializer = PathologyProfileSerializer(
                instance
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = PathologyProfileService.get_profile_by_id(pk)

        if not instance:
            return Response(
                {"error": "Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PathologyProfileSerializer(
            instance,
            data=request.data
        )

        if serializer.is_valid():

            updated_instance = (
                PathologyProfileService.update_profile(
                    instance,
                    serializer.validated_data
                )
            )

            response_serializer = (
                PathologyProfileSerializer(
                    updated_instance
                )
            )

            return Response(response_serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = PathologyProfileService.get_profile_by_id(pk)

        if not instance:
            return Response(
                {"error": "Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        PathologyProfileService.delete_profile(instance)

        return Response(
            {"message": "Profile deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
    
# ==================================
# Agency_(Master)_ViewSet
# ==================================

class AgencyViewSet(ViewSet):

    def list(self, request):

        queryset = AgencyService.get_all_agencies()

        serializer = AgencySerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = AgencyService.get_agency_by_id(pk)

        if not instance:
            return Response(
                {"error": "Agency not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AgencySerializer(instance)

        return Response(serializer.data)

    def create(self, request):

        serializer = AgencySerializer(
            data=request.data
        )

        if serializer.is_valid():

            instance = AgencyService.create_agency(
                serializer.validated_data
            )

            response_serializer = AgencySerializer(
                instance
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = AgencyService.get_agency_by_id(pk)

        if not instance:
            return Response(
                {"error": "Agency not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AgencySerializer(
            instance,
            data=request.data
        )

        if serializer.is_valid():

            updated_instance = (
                AgencyService.update_agency(
                    instance,
                    serializer.validated_data
                )
            )

            response_serializer = AgencySerializer(
                updated_instance
            )

            return Response(response_serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = AgencyService.get_agency_by_id(pk)

        if not instance:
            return Response(
                {"error": "Agency not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        AgencyService.delete_agency(instance)

        return Response(
            {"message": "Agency deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
# ==================================
# Machine_(Master)_ViewSet
# ==================================    

class MachineViewSet(ViewSet):

    def list(self, request):

        queryset = MachineService.get_all_machines()

        serializer = MachineSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = MachineService.get_machine_by_id(pk)

        if not instance:
            return Response(
                {"error": "Machine not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MachineSerializer(instance)

        return Response(serializer.data)

    def create(self, request):

        serializer = MachineSerializer(
            data=request.data
        )

        if serializer.is_valid():

            instance = MachineService.create_machine(
                serializer.validated_data
            )

            response_serializer = MachineSerializer(
                instance
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = MachineService.get_machine_by_id(pk)

        if not instance:
            return Response(
                {"error": "Machine not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MachineSerializer(
            instance,
            data=request.data
        )

        if serializer.is_valid():

            updated_instance = (
                MachineService.update_machine(
                    instance,
                    serializer.validated_data
                )
            )

            response_serializer = MachineSerializer(
                updated_instance
            )

            return Response(response_serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = MachineService.get_machine_by_id(pk)

        if not instance:
            return Response(
                {"error": "Machine not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        MachineService.delete_machine(instance)

        return Response(
            {"message": "Machine deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
    
# ==================================
# Machine_Parameter_ViewSet
# ==================================

from restapi.serializers.machine_parameter import (
    MachineParameterSerializer
)

from restapi.services.machine_parameter_service import (
    MachineParameterService
)

class MachineParameterViewSet(ViewSet):

    def list(self, request):

        queryset = (
            MachineParameterService
            .get_all_machine_parameters()
        )

        serializer = MachineParameterSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = (
            MachineParameterService
            .get_machine_parameter_by_id(pk)
        )

        if not instance:
            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MachineParameterSerializer(
            instance
        )

        return Response(serializer.data)

    def create(self, request):

        serializer = MachineParameterSerializer(
            data=request.data
        )

        if serializer.is_valid():

            instance = (
                MachineParameterService
                .create_machine_parameter(
                    serializer.validated_data
                )
            )

            response_serializer = (
                MachineParameterSerializer(
                    instance
                )
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = (
            MachineParameterService
            .get_machine_parameter_by_id(pk)
        )

        if not instance:
            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MachineParameterSerializer(
            instance,
            data=request.data
        )

        if serializer.is_valid():

            updated_instance = (
                MachineParameterService
                .update_machine_parameter(
                    instance,
                    serializer.validated_data
                )
            )

            response_serializer = (
                MachineParameterSerializer(
                    updated_instance
                )
            )

            return Response(
                response_serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = (
            MachineParameterService
            .get_machine_parameter_by_id(pk)
        )

        if not instance:
            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        MachineParameterService.delete_machine_parameter(
            instance
        )

        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
    
# ==================================
# Agency_Service_ViewSet
# ==================================

from restapi.serializers.agency_service import (
    AgencyServiceSerializer
)

from restapi.services.agency_service_service import (
    AgencyServiceService
)

class AgencyServiceViewSet(ViewSet):

    def list(self, request):

        queryset = (
            AgencyServiceService
            .get_all_agency_services()
        )

        serializer = AgencyServiceSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = (
            AgencyServiceService
            .get_agency_service_by_id(pk)
        )

        if not instance:
            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AgencyServiceSerializer(
            instance
        )

        return Response(serializer.data)

    def create(self, request):

        serializer = AgencyServiceSerializer(
            data=request.data
        )

        if serializer.is_valid():

            instance = (
                AgencyServiceService
                .create_agency_service(
                    serializer.validated_data
                )
            )

            response_serializer = (
                AgencyServiceSerializer(
                    instance
                )
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = (
            AgencyServiceService
            .get_agency_service_by_id(pk)
        )

        if not instance:
            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AgencyServiceSerializer(
            instance,
            data=request.data
        )

        if serializer.is_valid():

            updated_instance = (
                AgencyServiceService
                .update_agency_service(
                    instance,
                    serializer.validated_data
                )
            )

            response_serializer = (
                AgencyServiceSerializer(
                    updated_instance
                )
            )

            return Response(
                response_serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = (
            AgencyServiceService
            .get_agency_service_by_id(pk)
        )

        if not instance:
            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        AgencyServiceService.delete_agency_service(
            instance
        )

        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
    
# ==================================
# CLinic (Master)_ViewSet
# ==================================

from restapi.serializers.clinic import ClinicSerializer
from restapi.services.clinic_service import ClinicService

class ClinicViewSet(ViewSet):

    def list(self, request):

        queryset = ClinicService.get_all_clinics()

        serializer = ClinicSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = ClinicService.get_clinic_by_id(pk)

        if not instance:

            return Response(
                {"error": "Clinic not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ClinicSerializer(instance)

        return Response(serializer.data)

    def create(self, request):

        serializer = ClinicSerializer(
            data=request.data
        )

        if serializer.is_valid():

            instance = ClinicService.create_clinic(
                serializer.validated_data
            )

            response_serializer = ClinicSerializer(
                instance
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = ClinicService.get_clinic_by_id(pk)

        if not instance:

            return Response(
                {"error": "Clinic not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ClinicSerializer(
            instance,
            data=request.data
        )

        if serializer.is_valid():

            updated_instance = (
                ClinicService.update_clinic(
                    instance,
                    serializer.validated_data
                )
            )

            response_serializer = ClinicSerializer(
                updated_instance
            )

            return Response(
                response_serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = ClinicService.get_clinic_by_id(pk)

        if not instance:

            return Response(
                {"error": "Clinic not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        ClinicService.delete_clinic(instance)

        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
    

# ==================================
# Agency (Master)_ViewSet
# ==================================
    
from restapi.serializers.agency_clinic import (
    AgencyClinicSerializer
)

from restapi.services.agency_clinic_service import (
    AgencyClinicService
)


class AgencyClinicViewSet(ViewSet):

    def list(self, request):

        queryset = (
            AgencyClinicService.get_all()
        )

        serializer = (
            AgencyClinicSerializer(
                queryset,
                many=True
            )
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = (
            AgencyClinicService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = (
            AgencyClinicSerializer(instance)
        )

        return Response(serializer.data)

    def create(self, request):

        serializer = (
            AgencyClinicSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            instance = (
                AgencyClinicService.create(
                    serializer.validated_data
                )
            )

            response_serializer = (
                AgencyClinicSerializer(instance)
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = (
            AgencyClinicService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = (
            AgencyClinicSerializer(
                instance,
                data=request.data
            )
        )

        if serializer.is_valid():

            updated_instance = (
                AgencyClinicService.update(
                    instance,
                    serializer.validated_data
                )
            )

            response_serializer = (
                AgencyClinicSerializer(
                    updated_instance
                )
            )

            return Response(
                response_serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = (
            AgencyClinicService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        AgencyClinicService.delete(instance)

        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

# ==================================
# Test_Parameter_Link_ViewSet
# ==================================

from restapi.serializers.test_parameter_link import (
    TestParameterLinkSerializer
)

from restapi.services.test_parameter_link_service import (
    TestParameterLinkService
)

class TestParameterLinkViewSet(ViewSet):

    def list(self, request):

        queryset = (
            TestParameterLinkService.get_all()
        )

        serializer = (
            TestParameterLinkSerializer(
                queryset,
                many=True
            )
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = (
            TestParameterLinkService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = (
            TestParameterLinkSerializer(instance)
        )

        return Response(serializer.data)

    def create(self, request):

        serializer = (
            TestParameterLinkSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            instance = (
                TestParameterLinkService.create(
                    serializer.validated_data
                )
            )

            response_serializer = (
                TestParameterLinkSerializer(
                    instance
                )
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = (
            TestParameterLinkService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = (
            TestParameterLinkSerializer(
                instance,
                data=request.data
            )
        )

        if serializer.is_valid():

            updated_instance = (
                TestParameterLinkService.update(
                    instance,
                    serializer.validated_data
                )
            )

            response_serializer = (
                TestParameterLinkSerializer(
                    updated_instance
                )
            )

            return Response(
                response_serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = (
            TestParameterLinkService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        TestParameterLinkService.delete(
            instance
        )

        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

# ==================================
# Test_Sample_Link_ViewSet
# ==================================    

from restapi.serializers.test_sample_link import (
    TestSampleLinkSerializer
)

from restapi.services.test_sample_link_service import (
    TestSampleLinkService
)

class TestSampleLinkViewSet(ViewSet):

    def list(self, request):

        queryset = (
            TestSampleLinkService.get_all()
        )

        serializer = (
            TestSampleLinkSerializer(
                queryset,
                many=True
            )
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = (
            TestSampleLinkService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = (
            TestSampleLinkSerializer(instance)
        )

        return Response(serializer.data)

    def create(self, request):

        serializer = (
            TestSampleLinkSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            instance = (
                TestSampleLinkService.create(
                    serializer.validated_data
                )
            )

            response_serializer = (
                TestSampleLinkSerializer(
                    instance
                )
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = (
            TestSampleLinkService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = (
            TestSampleLinkSerializer(
                instance,
                data=request.data
            )
        )

        if serializer.is_valid():

            updated_instance = (
                TestSampleLinkService.update(
                    instance,
                    serializer.validated_data
                )
            )

            response_serializer = (
                TestSampleLinkSerializer(
                    updated_instance
                )
            )

            return Response(
                response_serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = (
            TestSampleLinkService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        TestSampleLinkService.delete(
            instance
        )

        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
# ==================================
# Test_Template_Link_ViewSet
# ================================== 

from restapi.serializers.test_template_link import (
    TestTemplateLinkSerializer
)

from restapi.services.test_template_link_service import (
    TestTemplateLinkService
)

class TestTemplateLinkViewSet(ViewSet):

    def list(self, request):

        queryset = (
            TestTemplateLinkService.get_all()
        )

        serializer = (
            TestTemplateLinkSerializer(
                queryset,
                many=True
            )
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        instance = (
            TestTemplateLinkService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = (
            TestTemplateLinkSerializer(instance)
        )

        return Response(serializer.data)

    def create(self, request):

        serializer = (
            TestTemplateLinkSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            instance = (
                TestTemplateLinkService.create(
                    serializer.validated_data
                )
            )

            response_serializer = (
                TestTemplateLinkSerializer(
                    instance
                )
            )

            return Response(
                response_serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        instance = (
            TestTemplateLinkService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = (
            TestTemplateLinkSerializer(
                instance,
                data=request.data
            )
        )

        if serializer.is_valid():

            updated_instance = (
                TestTemplateLinkService.update(
                    instance,
                    serializer.validated_data
                )
            )

            response_serializer = (
                TestTemplateLinkSerializer(
                    updated_instance
                )
            )

            return Response(
                response_serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        instance = (
            TestTemplateLinkService.get_by_id(pk)
        )

        if not instance:

            return Response(
                {"error": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        TestTemplateLinkService.delete(
            instance
        )

        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services.services import (
    create_patient,
    get_all_patients,
    get_patient_by_id,
    create_pending_shipment,
    get_all_pending_shipments,
    get_pending_by_id,
    create_schedule_shipping,
    get_all_schedule_shipping,
    move_to_shipped,
    get_all_shipped_shipments,
    move_to_received,
    get_all_received_shipments,
    get_all_activity_logs,
    create_manual_activity_log
)


# =========================================
# PATIENT VIEWS
# =========================================

class PatientView(APIView):

    def get(self, request):
        patients = get_all_patients()

        data = []
        for patient in patients:
            data.append({
                "id": patient.id,
                "patient_name": patient.patient_name,
                "age": patient.age,
                "sex": patient.sex,
                "mrn": patient.mrn,
                "cycle_id": patient.cycle_id
            })

        return Response(data)

    def post(self, request):
        patient = create_patient(request.data)

        return Response({
            "message": "Patient created successfully",
            "id": patient.id
        }, status=status.HTTP_201_CREATED)


# =========================================
# PENDING SHIPMENT VIEWS
# =========================================

class PendingShipmentView(APIView):

    def get(self, request):
        pendings = get_all_pending_shipments()

        data = []
        for item in pendings:
            data.append({
                "id": item.id,
                "sample_no": item.sample_no,
                "sample_type": item.sample_type,
                "test_code": item.test_code,
                "test_name": item.test_name,
                "service_name": item.service_name,
                "patient": item.patient.patient_name
            })

        return Response(data)

    def post(self, request):
        pending = create_pending_shipment(request.data)

        return Response({
            "message": "Pending Shipment created successfully",
            "id": pending.id
        }, status=status.HTTP_201_CREATED)
    


# =========================================
# ScheduleShippingView
# =========================================

class ScheduleShippingView(APIView):

    def get(self, request):

        schedules = get_all_schedule_shipping()

        data = []

        for item in schedules:

            data.append({
                "id": item.id,
                "pending_id": item.pending.id,
                "sample_no": item.pending.sample_no,
                "sample_type": item.pending.sample_type,
                "test_name": item.pending.test_name,
                "patient": item.pending.patient.patient_name,
                "ship_date": item.ship_date,
                "ship_time": item.ship_time,
                "dispatched_by": item.dispatched_by,
                "ship_to": item.ship_to
            })

        return Response(data)

    def post(self, request):

        schedule = create_schedule_shipping(
            request.data
        )

        return Response({
            "message": "Schedule Shipping created successfully",
            "id": schedule.id
        }, status=status.HTTP_201_CREATED)


# =========================================
# MOVE TO SHIPPED VIEW
# =========================================

class MoveToShippedView(APIView):

    def post(self, request):
        pending_id = request.data.get("pending_id")
        ship_to = request.data.get("ship_to")
        ship_by = request.data.get("ship_by")

        shipped = move_to_shipped(
            pending_id,
            ship_to,
            ship_by
        )

        return Response({
            "message": "Shipment moved to shipped successfully",
            "shipment_no": shipped.shipment_no
        }, status=status.HTTP_201_CREATED)


# =========================================
# SHIPPED SHIPMENT VIEW
# =========================================

class ShipmentShippedView(APIView):

    def get(self, request):
        shipments = get_all_shipped_shipments()

        data = []
        for item in shipments:
            data.append({
                "id": item.id,
                "shipment_no": item.shipment_no,
                "ship_date": item.ship_date,
                "sample_no": item.pending_shipment.sample_no,
                "patient": item.pending_shipment.patient.patient_name,
                "ship_to": item.ship_to
            })

        return Response(data)


# =========================================
# MOVE TO RECEIVED VIEW
# =========================================

class MoveToReceivedView(APIView):

    def post(self, request):
        shipped_id = request.data.get("shipped_id")
        status_value = request.data.get("status")
        result_value = request.data.get("result")

        received = move_to_received(
            shipped_id,
            status_value,
            result_value
        )

        return Response({
            "message": "Shipment moved to received successfully",
            "received_no": received.received_no
        }, status=status.HTTP_201_CREATED)


# =========================================
# RECEIVED SHIPMENT VIEW
# =========================================

class ShipmentReceivedView(APIView):

    def get(self, request):
        receiveds = get_all_received_shipments()

        data = []
        for item in receiveds:
            data.append({
                "id": item.id,
                "received_no": item.received_no,
                "receive_date": item.receive_date,
                "shipment_no": item.shipped_shipment.shipment_no,
                "status": item.status,
                "result": item.result
            })

        return Response(data)


# =========================================
# ACTIVITY LOGS VIEW
# =========================================

class ActivityLogsView(APIView):
    def get(self, request):
        logs = get_all_activity_logs()

        data = []

        for log in logs:
            data.append({
                "id": log.id,
                "ship_no": log.shipped_shipment.shipment_no if log.shipped_shipment else None,
                "ship_from": log.ship_from,
                "ship_to": log.ship_to,
                "ship_by": log.ship_by,
                "ship_date_time": log.ship_date_time,
            })

        return Response(data)
