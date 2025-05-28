from django.contrib import admin
from myapp.models import Domicilio, Morador

class MoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'sexo', 'idade', 'relacao_com_responsavel')
    list_filter = ('sexo', 'idade', 'relacao_com_responsavel')
    search_fields = ('nome', 'sobrenome')

admin.site.register(Domicilio)
admin.site.register(Morador, MoradorAdmin)
