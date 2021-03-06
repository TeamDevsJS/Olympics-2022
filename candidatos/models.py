from django.db import models

# Create your models here.





class CandidatoPresidente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    cedula = models.CharField(max_length=10)
    votos = models.IntegerField(null=True, blank=True, default=0)
    profesion = models.CharField(max_length=100)
    partido = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    propuesta_1 = models.CharField(max_length=200, blank=True, null=True)
    propuesta_2 = models.CharField(max_length=200, blank=True, null=True)
    propuesta_3 = models.CharField(max_length=200, blank=True, null=True)
    

    def __str__(self):
        return '{} {} ~ {}'.format(self.nombre, self.apellidos, self.votos)
    
    
class Propuestas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=800)
    propuestas = models.ForeignKey(CandidatoPresidente, on_delete=models.CASCADE, related_name='propuestas')