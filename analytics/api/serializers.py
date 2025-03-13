from rest_framework import serializers
from analytics.models import Entity, GeospatialData

# Entity Serializer
class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'

# GeospatialData Serializer
class GeospatialDataSerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)
    entity_id = serializers.PrimaryKeyRelatedField(
        queryset=Entity.objects.all(), source='entity', write_only=True
    )

    class Meta:
        model = GeospatialData
        fields = '__all__'
