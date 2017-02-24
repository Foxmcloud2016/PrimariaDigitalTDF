from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User

from .forms import AccionForm
from .models import Accion

# Create your views here.

class AccionCreateView(LoginRequiredMixin,CreateView):
    model = Accion
    template_name = "alta_accion.html"
    login_url = reverse_lazy('users:login')
    form_class = AccionForm
    success_url = reverse_lazy('acciones:lista')

    def form_valid(self,form):
        form.instance.usuario = self.request.user
        return super(AccionCreateView,self).form_valid(form)

class AccionListView(ListView):
    model = Accion
    template_name = "lista_acciones.html"

    def get_context_data(self,**kwargs):
        context = super(AccionListView,self).get_context_data(**kwargs)
        context['acciones'] = Accion.objects.filter(usuario = self.request.user)
        return context

