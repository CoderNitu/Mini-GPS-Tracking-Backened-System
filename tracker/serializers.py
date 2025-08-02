from rest_framework import serializers
from .models import Device, LocationData

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class LocationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationData
        fields = '__all__'
