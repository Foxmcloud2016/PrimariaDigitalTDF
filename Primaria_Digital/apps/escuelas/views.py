from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import Escuela
from .forms import EscuelaForm

# Create your views here.
class EscuelaCreateView(CreateView):
    model = Escuela
    template_name = "alta.html"
    form_class = EscuelaForm
    success_url = reverse_lazy('main:home')

class EscuelaUpdateView(UpdateView):
    model = Escuela
    template_name = "alta.html"
    form_class = EscuelaForm
    success_url = reverse_lazy('main:home')
