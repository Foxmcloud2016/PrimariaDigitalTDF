# shortcuts para renderizar
from django.shortcuts import render
# Vistas genericas
from django.views.generic import TemplateView, View, FormView, CreateView
# Modelos utilizados
from apps.escuelas.models import Escuela
from .models import Adm, Dispositivo
# Para retornar una respuesta en tipo JSON , al usar AJAX
from django.http import JsonResponse
# Para resolver urls basados en nombre
from django.core.urlresolvers import reverse_lazy, reverse
# Necesario para renderizar un template con el contexto apropiado y que lo devuelva en
# string para enviarlo a traves de ajax.
from django.template.loader import render_to_string
# Clases Formularios
from .forms import DispositivoUnicoForm, NetbookForm
# Mixin para agregar funcionalidad a las vistas
# Es necesario estar logeado para acceder a esta vista.
from django.contrib.auth.mixins import LoginRequiredMixin


# VIEW CREATE DISPOSITIVOS
# Con esta vista cargamos todos los dispositivos unicos que existen en un ADM
class DispositivoCreateView(LoginRequiredMixin, FormView):
    model = Dispositivo
    template_name = "alta_dispositivo.html"
    form_class = DispositivoUnicoForm
    success_url = reverse_lazy('dispositivos:lista')
    login_url = reverse_lazy('users:login')

    # Recibimos las variables por parametro y la agregamos al conexto de la
    # vista.
    def get(self, request, *args, **kwargs):
        context = super(DispositivoCreateView, self).get_context_data(**kwargs)
        # se agrega el Adm al contexto
        context['adm'] = Adm.objects.get(id=context['id_adm'])
        # Agregamos el ADM al objeto DispositivoCreateView
        self.id_adm = context['id_adm']
        # Devolvemos la pagina con el contexto modificado
        return render(request, self.template_name, context)

    def form_valid(self, form):  # Una vez que el formulario es valido...
        form.save()  # Guardamos el objeto del formulario.
        # Retornamos el formulario vacio
        return super(DispositivoCreateView, self).form_valid(form)

# Vista para alta de netbooks
# Esta vista se encarga de dar de alta una netbook en un adm escolar.


class NetbookCreateView(LoginRequiredMixin, FormView):
    model = Dispositivo
    template_name = "alta_netbooks.html"
    form_class = NetbookForm
    success_url = reverse_lazy('dispositivos:lista')
    login_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        # Recibimos las variables por parametro y la agregamos al conexto de la
        # vista.
        # se agrega el Adm al contexto
        context = super(NetbookCreateView, self).get_context_data(**kwargs)
        # Agregamos el ADM al objeto DispositivoCreateView
        context['adm'] = Adm.objects.get(id=context['id_adm'])
        # Devolvemos la pagina con el contexto modificado
        self.id_adm = context['id_adm']
        return render(request, self.template_name, context)

    def form_valid(self, form):
        form.save()  # Se guarda el objeto.
        form = NetbookForm()  # Se crea un formulario nuevo vacio
        return super(NetbookCreateView, self).form_valid(form)

# Vista para Crear Adm para la escuela


class CreateAdm(LoginRequiredMixin, View):

    login_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        # Obtenemos el valor del id de la escuela a traves de GET que nos envia
        # AJAX
        id_escuela = request.GET['id_escuela']
        # Creamos la variable anio para generar el anio
        anio = '{}-01-01'.format(request.GET['anio_recepcion'])
        # Traemos el objeto Escuela al que va  a estar asociado el adm
        escuela = Escuela.objects.get(id=id_escuela)
        # Creamos el ADM
        adm = Adm.objects.create(
            escuela=escuela,
            anio_recepcion=anio)
        adm.save()  # Guardamos
        mensaje = {'exito': '¡Adm agregado con exito!'}
        # Se envia a la page como un adm agregado con exito
        return JsonResponse(mensaje)

# VIEW DISPOSITIVOS
# Vista Principal , se les envia todos los establecimientos.
# Habria que mostrar la data dependiendo el usuario


class DispositivosView(LoginRequiredMixin, TemplateView):
    template_name = "lista_dispositivos.html"
    login_url = reverse_lazy('users:login')

    # Modificamos el get_context_data para que agregue las escuelas en el
    # contexto
    def get_context_data(self, **kwargs):
        context = super(DispositivosView, self).get_context_data(**kwargs)
        context['escuelas'] = Escuela.objects.all()
        return context

# AJAX , se utiliza para renderizar la pagina que va a ser enviadar por HTML a la vista
# lista_dispositivos.html ya que esta posee el ajax


class EscuelaDispositivosView(LoginRequiredMixin, View):

    login_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        # Buscamos la escuela
        escuela_elegida = Escuela.objects.get(id=request.GET['id_escuela'])
        # Variable de contexto vacia para llenar con los datos necesarios
        context = {}
        # SI el adm no existe entonces...
        if not Adm.objects.filter(escuela=escuela_elegida).exists():
            # Se agrega el valor False a una key adm del contexto a enviar.
            context['adm'] = False
        else:  # Sino
            # Traemos el Adm de la escuela
            adm = Adm.objects.get(escuela=escuela_elegida)
            # le agregamos True , mirar datos_dispositivos.html para entender
            context['adm'] = True
            # Si existe un servidor
            if Dispositivo.objects.filter(adm=adm, tipo=1).exists():
                # Pongo toda la data del servidor
                context['servidor'] = Dispositivo.objects.get(adm=adm, tipo=1)
            else:
                # Sino mando bandera de que no existe servidor para ese ADM
                context['servidor'] = False
            # Si existe una camara
            if Dispositivo.objects.filter(adm=adm, tipo=2).exists():
                # Pongo toda la data del camara
                context['camara'] = Dispositivo.objects.get(adm=adm, tipo=2)
                # Sino mando bandera de que no existe camara para ese ADM
            else:
                context['camara'] = False
                # Si existe un impresora
            if Dispositivo.objects.filter(adm=adm, tipo=3).exists():
                # Pongo toda la data del impresora
                context['impresora'] = Dispositivo.objects.get(adm=adm, tipo=3)
                # Sino mando bandera de que no existe impresora para ese ADM
            else:
                context['impresora'] = False
                # Si existe un cañon
            if Dispositivo.objects.filter(adm=adm, tipo=4).exists():
                # Pongo toda la data del cañon
                context['canon'] = Dispositivo.objects.get(adm=adm, tipo=4)
                # Sino mando bandera de que no existe cañon para ese ADM
            else:
                context['canon'] = False
                #Si existe un Monitor
            if Dispositivo.objects.filter(adm=adm, tipo=6).exists():
                # Pongo toda la data del Monitor
                context['monitor'] = Dispositivo.objects.get(adm=adm, tipo=6)
                # Sino mando bandera de que no existe Monitor para ese ADM
            else:
                context['monitor'] = False
            #Si existe un pizarra
            if Dispositivo.objects.filter(adm=adm, tipo=7).exists():
                # Pongo toda la data del pizarra
                context['pizarra'] = Dispositivo.objects.get(adm=adm, tipo=7)
                # Sino mando bandera de que no existe pizarra para ese ADM
            else:
                context['pizarra'] = False
            # Agregar al contexto las netbooks
            context['netbooks'] = Dispositivo.objects.filter(
                adm=adm, tipo=5).order_by('n_m')
            # Agregar al contexto el adm
            context['adm_id'] = adm
        # Todo lo resultante del contexto se envia al html para construir el html a enviar
        # por AJAX
        html = (render_to_string('datos_dispositivos.html', context))
        # Enviar como Json el html resultante.
        return JsonResponse({'html': html})


"""
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
