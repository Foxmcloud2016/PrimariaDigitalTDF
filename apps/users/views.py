from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, View
from .forms import LoginForm,RegisterForm
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib.auth import login,authenticate,logout

class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        user = form.save()
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request,user)
        return super(RegisterView,self).form_valid(form)

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
        login(self.request,user)
        return super(LoginView,self).form_valid(form)

class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('home'))
