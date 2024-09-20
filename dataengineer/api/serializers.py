from rest_framework import serializers
from dataengineer.models import ImageModel

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['id', 'name', 'image','created_at']  # Specify the fields to be serialized
