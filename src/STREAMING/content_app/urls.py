from rest_framework.routers import DefaultRouter
from .views import ContentViewSet

# commit pra salvar alteraçoes do STREAMING
router = DefaultRouter()
router.register(r'contents', ContentViewSet)

urlpatterns = router.urls