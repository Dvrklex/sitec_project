from django.db import models
from enumchoicefield import EnumChoiceField
from .choises import DuracionMateria
# Create your models here.

class Carrera(models.Model):
    DURACION = (
            (1, "Uno"),
            (2, "Dos"),
            (3, "Tres"),
        )
    
    nombre = models.CharField(
        
        max_length=50,
        verbose_name="Nombre de la carrera"
        )
    
    duracion = models.IntegerField(verbose_name="Duracion", choices=DURACION)
    created_at = models.DateTimeField(verbose_name='Creado el',auto_now_add=True)    
    updated_at = models.DateTimeField(verbose_name='Actualizado el',auto_now=True)

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
    
    def __str__(self):  
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre de la materia"
        )
    duracion = EnumChoiceField(
        DuracionMateria,
        verbose_name="Duracion de la materia",
        default=DuracionMateria.SEMESTRAL
        )
    carrera = models.ForeignKey(Carrera,verbose_name='Carrera', on_delete=models.CASCADE, related_name='materias')
    created_at = models.DateTimeField(verbose_name='Creado el',auto_now_add=True)    
    updated_at = models.DateTimeField(verbose_name='Actualizado el',auto_now=True)

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"
        unique_together = ('nombre', 'carrera')
    
    def __str__(self):  
        return self.nombre

    def get_nombre_duracion(self):
        return f'{self.nombre} - {self.duracion}'