from rest_framework import viewsets
from analytics.models import Entity, GeospatialData
from .serializers import EntitySerializer, GeospatialDataSerializer

class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class GeospatialDataViewSet(viewsets.ModelViewSet):
    queryset = GeospatialData.objects.all()
    serializer_class = GeospatialDataSerializer
