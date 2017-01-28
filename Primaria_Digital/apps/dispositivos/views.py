from django.shortcuts import render
from django.views.generic import TemplateView, View
from apps.escuelas.models import Escuela
from .models import Adm , Dispositivo
from django.http import JsonResponse
from django.core import serializers
from django.template.loader import render_to_string
# Create your views here.

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
