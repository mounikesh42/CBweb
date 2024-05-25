from rest_framework.routers import DefaultRouter
from django.urls import path
from drones.api.views import DroneViewSet


router = DefaultRouter()


router.register(r'drones', DroneViewSet)


urlpatterns = [
    
]

urlpatterns += router.urls
