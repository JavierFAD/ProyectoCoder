from django.db import models
from operario.models import Operario

class Herramienta(models.Model):
    designacion   = models.CharField(max_length=50, verbose_name='Designación')
    rastreo       = models.IntegerField(help_text='Número de identificación')
    asignado      = models.DateField(auto_now=True, blank=True, null=True, help_text='Formato = mm/dd/aaaa')
    operario      = models.ForeignKey(Operario,blank=True, null=True, on_delete=models.CASCADE, related_name='herramientas')
    descripcion   = models.TextField(verbose_name='Descripción')
    calibracion   = models.DateField(blank=True, null=True, help_text='Fecha de calibración. Formato = mm/dd/aaaa', verbose_name='Calibración')
    imagen = models.ImageField(blank=True, default="herramienta.png", null=True, upload_to="herramientas")
    
    def __str__(self) -> str:
        return self.designacion + ' | ' + str(self.rastreo) + ' | ' + 'Asignado a: ' + str(self.operario) + ' --> Fecha de asignado: ' + str(self.asignado)
    