from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from myapp.api import InformacaoDomicilioViewSet, InformacaoMoradorViewSet

router = DefaultRouter()
router.register(r'informacao-domicilio', InformacaoDomicilioViewSet)
router.register(r'informacao-morador', InformacaoMoradorViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('', views.home, name='home'),
]