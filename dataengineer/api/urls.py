from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageModelViewSet

router = DefaultRouter()
router.register(r'images', ImageModelViewSet)  # Register the ViewSet with the router

urlpatterns = [
    path('', include(router.urls)),  # Include the ViewSet routes
]