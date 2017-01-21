from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.core.urlresolvers import reverse_lazy

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "home.html"
    login_url = reverse_lazy('users:login')
    
