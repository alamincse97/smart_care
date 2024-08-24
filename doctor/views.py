from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializers_class = serializers.SpecializationSerializer 

class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializers_class = serializers.DesignationSerializer
    
class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializers_class = serializers.AvailableTimeSerializer

class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializers_class = serializers.DoctorSerializer
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializers_class = serializers.ReviewSerializer