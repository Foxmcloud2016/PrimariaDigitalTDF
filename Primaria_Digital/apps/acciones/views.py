from django.shortcuts import render
from django.views.generic import CreateView
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
    success_url = reverse_lazy('acciones:alta')

    def form_valid(self,form):
        form.instance.usuario = self.request.user
        return super(AccionCreateView,self).form_valid(form)




    
