from django.db import models

class Consumible(models.Model):
    designacion   = models.CharField(max_length=50)
    descripcion   = models.CharField(max_length=200, help_text='Descripción breve del Producto')
    cantidad      = models.IntegerField(help_text='Ingrese la cantidad del producto')
    unidad        = models.CharField(max_length=10, default='c/u',help_text='Ingrese la unidad(Ej: Kg, m, Lts)')
    vencimiento   = models.DateField(null=True,blank=True)
    lote          = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.designacion + ' -----> ' + str(self.cantidad) + self.unidad  + ' | ' + self.descripcion
    
