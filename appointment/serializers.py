from rest_framework import serializer
from . import models

class AppointmentSerializer(serializer.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = '__all__'