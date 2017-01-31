from django.shortcuts import render
from django.views.generic import TemplateView, View, CreateView
from apps.escuelas.models import Escuela
from .models import Adm , Dispositivo
from django.http import JsonResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
# Create your views here.


### VIEW ADM

class CreateAdm(View):

    def get(self,request,*args,**kwargs):
        id_escuela = request.GET['id_escuela']
        anio = '{}-01-01'.format(request.GET['anio_recepcion'])
        escuela = Escuela.objects.get(id = id_escuela)
        adm = Adm.objects.create(
            escuela = escuela,
            anio_recepcion = anio)
        adm.save()
        mensaje = {'exito': '¡Adm agregado con exito!'}
        return JsonResponse(mensaje)

### VIEW DISPOSITIVOS

class DispositivosView(TemplateView):
    template_name = "lista_dispositivos.html"

    def get_context_data(self,**kwargs):
        context = super(DispositivosView,self).get_context_data(**kwargs)
        context['escuelas'] = Escuela.objects.all()
        return context

class EscuelaDispositivosView(View):

    def get(self,request,*args,**kwargs):
        escuela_elegida = Escuela.objects.get(id = request.GET['id_escuela'])

        context = {}
        if not Adm.objects.filter(escuela = escuela_elegida).exists():
            context['adm'] = False
        else:
            adm = Adm.objects.filter(escuela = escuela_elegida)
            context['adm'] = True
            if Dispositivo.objects.filter(adm = adm , tipo = 1).exists():
                context['servidor'] = Dispositivo.objects.get(adm = adm , tipo = 1)
            else:
                context['servidor'] = False
            if Dispositivo.objects.filter(adm = adm , tipo = 2).exists():    
                context['camara'] = Dispositivo.objects.get(adm = adm , tipo = 2)
            else:
                context['camara'] = False
            if Dispositivo.objects.filter(adm = adm , tipo = 3).exists():
                context['impresora'] = Dispositivo.objects.get(adm = adm , tipo = 3)
            else:
                context['impresora'] = False
            if Dispositivo.objects.filter(adm = adm , tipo = 4).exists():    
                context['canon'] = Dispositivo.objects.get(adm = adm , tipo = 4)
            else:
                context['canon'] = False
            context['netbooks'] = Dispositivo.objects.filter(adm = adm , tipo = 5)
            print(context['camara'])

        html = (render_to_string('datos_dispositivos.html',context))
        return JsonResponse({'html' : html})
