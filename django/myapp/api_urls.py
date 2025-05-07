from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.api import InformacaoDomicilioViewSet

router = DefaultRouter()
router.register(r'informacoes-domicilio', InformacaoDomicilioViewSet, basename='informacao-domicilio')

urlpatterns = [
    path('', include(router.urls)),
]
