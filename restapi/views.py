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