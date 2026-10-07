from django.contrib import admin
from .models import Cliente, plan


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'direccion', 'fecha_registro', 'plan')
    search_fields = ('nombre', 'apellido', 'email', 'telefono')
    list_filter = ('plan',)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'duracion_meses')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('duracion_meses',)



admin.site.register(Cliente, ClienteAdmin)
admin.site.register(plan, PlanAdmin)



