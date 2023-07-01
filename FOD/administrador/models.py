from django.db import models
from django.contrib.auth.models import User

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True, default='usuario.png')