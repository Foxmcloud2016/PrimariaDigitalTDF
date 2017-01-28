from django.db import models

from apps.escuelas.models import Escuela
# Create your models here.

class Adm(models.Model):

    escuela = models.OneToOneField(Escuela)
    anio_recepcion = models.DateField()

    class Meta:
        verbose_name = "Adm"
        verbose_name_plural = "Adms"

    def __str__(self):
        return "{} - {}".format(self.escuela,self.anio_recepcion)


class Servidor(models.Manager):
    pass

class Dispositivo(models.Model):

    adm = models.ForeignKey(Adm)
    tipo = models.IntegerField()
    estado = models.IntegerField()
    n_m = models.IntegerField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    n_s = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"

    def __str__(self):
        return "{} - {}".format(self.adm.escuela.nombre,self.get_tipo(self.tipo))

    def get_tipo(self,tipo):
        if tipo == 1:
            return "Servidor"
        if tipo == 2:
            return "Cañon"
        if tipo == 3:
            return "Impresora"
        if tipo == 4:
            return "Camara"
        if tipo == 5:
            return "Netbook"

