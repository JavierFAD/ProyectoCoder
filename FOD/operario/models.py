from django.db import models
from encargado.models import Encargado



class Operario(models.Model):
    nombre      = models.CharField(max_length=80,blank=True,null=True, default='')
    apellido    = models.CharField(max_length=60)
    legajo      = models.IntegerField()
    encargado   = models.ForeignKey(Encargado, on_delete=models.CASCADE)
    funcion     = models.TextField()
    imagen = models.ImageField(blank=True, default="operario.png", null=True, upload_to="operarios")

    
    def __str__(self) -> str:
        return self.apellido + ', ' + self.nombre+ ' | ' + str(self.legajo) + ' | Encargado: ' + str(self.encargado) 
    

