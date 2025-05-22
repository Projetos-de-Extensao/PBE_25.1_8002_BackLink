from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.api import DomicilioViewSet, MoradorViewSet

router = DefaultRouter()
router.register(r'domicilio',DomicilioViewSet, basename='domicilio')

urlpatterns = [
    path('', include(router.urls)),
]
