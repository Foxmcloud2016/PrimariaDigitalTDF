from django.shortcuts import render
from django.views.generic import TemplateView, View, FormView, CreateView
from apps.escuelas.models import Escuela
from .models import Adm , Dispositivo
from django.http import JsonResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy,reverse
from django.template.loader import render_to_string
from .forms import DispositivoUnicoForm,NetbookMasiveForm

# Create your views here.


### VIEW CREATE DISPOSITIVOS
TIPOS_DISPOSITIVO = {
    'servidor' : 1,
    'canon' : 2,
    'impresora' : 3,
    'camara' : 4,
}

class DispositivoCreateView(FormView):
    model = Dispositivo
    template_name = "alta_dispositivo.html"
    form_class = DispositivoUnicoForm
    success_url = reverse_lazy('dispositivos:lista')

    def get(self,request,*args,**kwargs):
        context = super(DispositivoCreateView,self).get_context_data(**kwargs)
        context['adm'] = Adm.objects.get(id=context['id_adm'])
        self.id_adm = context['id_adm']
        print(context['n_tipo'])
        return render(request,self.template_name,context)

    def form_valid(self,form):
        form.save()
        return super(DispositivoCreateView,self).form_valid(form)

class NetbookFormMassiveView(FormView):
    model = Dispositivo
    template_name = "alta_netbooks.html"
    form_class = NetbookMasiveForm
    success_url = reverse_lazy('dispositivos:lista')

    def get(self,request,*args,**kwargs):
        context = super(NetbookFormMassiveView,self).get_context_data(**kwargs)
        context['adm'] = Adm.objects.get(id=context['id_adm'])
        self.id_adm = context['id_adm']
        return render(request,self.template_name,context)

    def form_valid(self,form):
        form_content = form.cleaned_data
        modelo = form_content.pop('modelo')
        marca = form_content.pop('marca')
        adm = Adm.objects.get(id=form_content.pop('adm'))
        index = 1
        try:
            for netbook in form_content.values():
                Dispositivo.objects.create(adm = adm,tipo = 5,n_m = index,
                marca = marca,modelo = modelo,n_s = netbook)
                index += 1
        except IntegrityError:
            super(NetbookFormMassiveView,self).form_invalid(form)
        return super(NetbookFormMassiveView,self).form_valid(form)

"""
class NetbookCreateView(FormView):
    model = Dispositivo
    template_name = "alta_netbooks.html"
    form_class = formset_factory(NetbooksForm,extra=2)
    success_url = reverse_lazy('dispositivos:lista')

    def get(self,request,*args,**kwargs):
        context = super(NetbookCreateView,self).get_context_data(**kwargs)
        context['adm'] = Adm.objects.get(id=context['id_adm'])
        formset = context['form']
        print("Este es", self.form_class)
        formset = self.form_class(initial=[{
                'marca':'marca',
                'modelo':'modelo',
            }
            ])
        context['form'] = formset
        self.id_adm = context['id_adm']
        return render(request,self.template_name,context)

    def form_valid(self,form):
        print(form.is_valid())
        return super(NetbookCreateView,self).form_valid(form)

"""
"""
class DispositivoCreateView(CreateView):
    model = Dispositivo
    template_name = "alta_dispositivo.html"
    form_class = DispositivoUnicoForm
    success_url = reverse_lazy('dispositivos:lista')

    def get(self,request,*args,**kwargs):
        print(request.GET['id_adm'])
"""
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
            adm = Adm.objects.get(escuela = escuela_elegida)
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
            context['netbooks'] = Dispositivo.objects.filter(adm = adm , tipo = 5).order_by('n_m')
            context['adm_id'] = adm


        html = (render_to_string('datos_dispositivos.html',context))
        return JsonResponse({'html' : html})
