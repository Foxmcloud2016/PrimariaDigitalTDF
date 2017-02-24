from django.db import models
from apps.escuelas.models import Escuela
from django.contrib.auth.models import User

# Create your models here.
class Accion(models.Model):

    escuela = models.ForeignKey(Escuela)
    usuario = models.ForeignKey(User)
    accion = models.TextField()
    observaciones = models.TextField(null=True,default=None)
    fecha = models.DateTimeField()
    realizada = models.BooleanField(default=True)
    programada = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Accion"
        verbose_name_plural = "Acciones"

    def __str__(self):
        return "{} - {}".format(self.escuela,self.usuario)
    