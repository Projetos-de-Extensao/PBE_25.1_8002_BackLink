from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.api import DomicilioViewSet, MoradorViewSet
from . import views

router = DefaultRouter()
router.register(r'domicilio', DomicilioViewSet)
router.register(r'morador', MoradorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.home, name='home'),
]