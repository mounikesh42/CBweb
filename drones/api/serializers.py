from rest_framework import serializers
from drones.models import Drone

class DroneeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        fields = ("company_name","drone_description","droneid","expiry")