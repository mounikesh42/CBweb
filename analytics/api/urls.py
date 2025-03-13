from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntityViewSet, GeospatialDataViewSet

router = DefaultRouter()
router.register(r'entities', EntityViewSet)
router.register(r'geospatial-data', GeospatialDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
