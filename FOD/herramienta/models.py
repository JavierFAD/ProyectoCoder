from django.db import models
from operario.models import Operario

class Herramienta(models.Model):
    designacion   = models.CharField(max_length=50)
    rastreo       = models.IntegerField(help_text='Número de Rastreo')
    asignado      = models.DateField(auto_now=True, blank=True, null=True, help_text='Formato = mm/dd/aaaa')
    operario      = models.ForeignKey(Operario,blank=True, null=True, on_delete=models.CASCADE, related_name='herramientas')
    descripcion   = models.TextField()
    calibracion   = models.DateField(blank=True, null=True, help_text='Fecha de calibración. Formato = mm/dd/aaaa')
    
    def __str__(self) -> str:
        return self.designacion + ' | ' + str(self.rastreo) + ' | ' + 'Asignado a: ' + str(self.operario) + ' --> Fecha de asignado: ' + str(self.asignado)
    