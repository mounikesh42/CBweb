from rest_framework import viewsets
from dataengineer.models import ImageModel
from .serializers import ImageModelSerializer

class ImageModelViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()  
    serializer_class = ImageModelSerializer  