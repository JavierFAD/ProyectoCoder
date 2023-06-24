from django.db import models

class Encargado(models.Model):
    nombre      = models.CharField(max_length=80,blank=True,null=True, default='')
    apellido    = models.CharField(max_length=60)
    legajo      = models.IntegerField()
    sector      = models.CharField(max_length=100)
    funcion     = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.apellido +', '+ self.nombre + ' | ' + str(self.legajo) + ' | ' + self.sector
    

