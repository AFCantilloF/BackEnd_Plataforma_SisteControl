from django.db import models

# Create your models here.

class Niveles(models.Model):
    nivel = models.CharField(max_length=50)

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    Tel = models.CharField(max_length=10)
    pasword = models.CharField(max_length=20)
    id_nivel = models.ForeignKey(Niveles, null=True, on_delete=models.CASCADE)


