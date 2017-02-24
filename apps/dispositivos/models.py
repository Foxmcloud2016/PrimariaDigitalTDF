from django.db import models
# Traemos el Modelo Escuela
from apps.escuelas.models import Escuela

class Adm(models.Model):

    escuela = models.OneToOneField(Escuela)
    anio_recepcion = models.DateField()

    class Meta:
        verbose_name = "Adm"
        verbose_name_plural = "Adms"

    def __str__(self):
        return "{} - {}".format(self.escuela.nombre, self.anio_recepcion)


class Dispositivo(models.Model):

    adm = models.ForeignKey(Adm)
    tipo = models.IntegerField()
    estado = models.IntegerField(default=1)
    n_m = models.IntegerField(null=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    n_s = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"

    def __str__(self):
        return "{} - {}".format(self.adm.escuela.nombre,
                                self.get_tipo(self.tipo))

    def get_tipo(self, tipo):
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
        if tipo == 6:
            return "Monitor"
        if tipo == 7:
            return "Pizarra"
