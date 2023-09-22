from django.db import models

# Create your models here.
class Curso(models.Model):
    
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()

class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    mail=models.EmailField()
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    mail=models.EmailField()
    profesion=models.CharField(max_length=30)

class Entreglable(models.Model):
    nombre=models.CharField(max_length=30)
    fechDeEntrega=models.DateField()
    entregado=models.BooleanField()

        

