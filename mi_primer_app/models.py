from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    deporte = models.CharField(max_length=50)
        
    def __str__(self):
        return f"{self.nombre} {self.apellido} (enseña: {self.deporte})"
    
class Deporte(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100)
    dias = models.CharField(max_length=100)
    horarios = models.CharField(max_length=20)
   
    def __str__(self):
        return self.nombre
    
class Atleta(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    deporte =models.CharField(max_length=100)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"
    
class Otra_actividad(models.Model):
    nombre = models.CharField(max_length=20)
    profesor = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.nombre} {self.profesor}'