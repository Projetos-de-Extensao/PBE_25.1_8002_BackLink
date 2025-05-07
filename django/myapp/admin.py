from django.contrib import admin
from .models import InformacaoDomicilio
from myapp.models import InformacaoMorador

@admin.register(InformacaoMorador)
class InformacaoMoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'sexo', 'idade')

admin.site.register(InformacaoDomicilio)