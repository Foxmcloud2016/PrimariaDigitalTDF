from django.db import models

# Create your models here.

class Escuela(models.Model):

    nombre = models.CharField(max_length=80)
    cue = models.IntegerField()
    domicilio = models.CharField(max_length=80)
    telefono = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Escuela"
        verbose_name_plural = "Escuelas"

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.cue)
        #return "%s - %d" % (self.escuela,self.cue) 
     