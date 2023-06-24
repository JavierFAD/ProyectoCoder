from django.contrib import admin
from .models import Herramienta
# Register your models here.
@admin.register(Herramienta)
class HerramientaAdmin(admin.ModelAdmin):
    list_display = [
        'designacion',
        'operario',
        'asignado',
        'rastreo',
    ]
    search_fields = ('rastreo',)
    search_fields = ('operario',)
    ordering = ('designacion', 'operario', 'rastreo')