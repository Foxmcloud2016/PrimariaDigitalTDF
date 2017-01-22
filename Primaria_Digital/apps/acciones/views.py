from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy

from .forms import AccionForm
from .models import Accion

# Create your views here.

class AccionCreateView(LoginRequiredMixin,CreateView):
    model = Accion
    template_name = "alta.html"
    login_url = reverse_lazy('users:login')
    form_class = AccionForm

    
