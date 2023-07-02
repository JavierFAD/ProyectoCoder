from django.db import models

class Consumible(models.Model):
    designacion   = models.CharField(max_length=50, verbose_name='Designación', help_text='Nombre comercial del producto')
    descripcion   = models.CharField(max_length=200, verbose_name='Descripción', help_text='Descripción breve del Producto')
    cantidad      = models.IntegerField(help_text='Ingrese la cantidad del producto')
    unidad        = models.CharField(max_length=10, default='c/u',help_text='Ingrese la unidad(Ej: Kg, m, Lts)')
    vencimiento   = models.DateField(null=True,blank=True, help_text='Formato dd/mm/aa')
    lote          = models.CharField(max_length=30)
    especificacion= models.TextField(blank=True, help_text='(Data Sheet info)')
    imagen = models.ImageField(blank=True, null=True, upload_to='consumibles', default='consumible.png')
    
    
    def __str__(self) -> str:
        return self.designacion + ' -----> ' + str(self.cantidad) + self.unidad  + ' | ' + self.descripcion
    
