from rest_framework import viewsets
from analytics.models import Entity, GeospatialData
from .serializers import EntitySerializer, GeospatialDataSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return only the entities associated with the logged-in user.
        """
        return Entity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Set the logged-in user as the entity owner when creating a new entity.
        """
        serializer.save(user=self.request.user)


class GeospatialDataViewSet(viewsets.ModelViewSet):
    queryset = GeospatialData.objects.all()
    serializer_class = GeospatialDataSerializer
