from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from .serializers import DroneeSerializer,DroneDataSerializer
from drones.models import Drone,DroneData
from rest_framework.filters import SearchFilter

class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all().order_by('-id')
    serializer_class = DroneeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    filter_backends = [SearchFilter]
    search_fields = ['skills']

    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE', 'PUT']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        queryset = Drone.objects.filter(manufacturer=user).order_by('-id')
        skills = self.request.query_params.get('skills', None)
        if skills:
            queryset = queryset.filter(skills__icontains=skills)
        return queryset



class DroneDataViewSet(viewsets.ModelViewSet):
    queryset = DroneData.objects.all()
    serializer_class = DroneDataSerializer