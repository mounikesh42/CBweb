from rest_framework.routers import DefaultRouter
from django.urls import path
from drones.api.views import DroneViewSet,DroneDataViewSet


router = DefaultRouter()


router.register(r'drones', DroneViewSet)
router.register(r'dronedata', DroneDataViewSet)
urlpatterns = [
    
]

urlpatterns += router.urls
