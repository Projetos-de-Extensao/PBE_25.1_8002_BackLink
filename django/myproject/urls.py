
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # URLs tradicionais
    path('api/', include('myapp.api_urls')),  # URLs da API
    path('api-auth/', include('rest_framework.urls')), 
     path('api/token/', obtain_auth_token, name='api_token_auth'), # Login para a API
    
]