from django.contrib import admin
from myapp.models import Domicilio, Morador

@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'sexo', 'idade', 'domicilios_list')

    def domicilios_list(self, obj):
        return ", ".join(str(dom) for dom in obj.domicilios.all())
    domicilios_list.short_description = "Domicilios"

admin.site.register(Domicilio)