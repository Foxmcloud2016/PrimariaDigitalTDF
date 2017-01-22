from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Escuela
from .forms import EscuelaForm

# Create your views here.
class EscuelaCreateView(LoginRequiredMixin,CreateView):
    model = Escuela
    template_name = "alta.html"
    form_class = EscuelaForm
    success_url = reverse_lazy('main:home')
    login_url = reverse_lazy('users:login')    

class EscuelaUpdateView(LoginRequiredMixin,UpdateView):
    model = Escuela
    template_name = "alta.html"
    form_class = EscuelaForm
    success_url = reverse_lazy('main:home')
    login_url = reverse_lazy('users:login')

class ListaEscuelasView(LoginRequiredMixin,TemplateView):
    template_name = "listado_colegios.html"
    login_url = reverse_lazy('users:login')

    def get_context_data(self,**kwargs):
        context = super(ListaEscuelasView,self).get_context_data(**kwargs)
        context['escuelas'] = Escuela.objects.all()
        return context
