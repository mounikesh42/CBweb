from rest_framework import serializers
from drones.models import Drone,DroneData

class DroneeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        fields = ("company_name","drone_description","droneid","expiry","live")


class DroneDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneData
        fields = '__all__'