from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')
        widgets = {
            'username': forms.TextInput(attrs={
                'type': 'text',
                'placeholder':'Username'
                }),
            'email': forms.TextInput(attrs={
                'type': 'email',
                'placeholder':'Ingrese Email'
                }),
            'password': forms.TextInput(attrs={
                'type': 'password',
                'placeholder':'Ingrese contraseña'
                })
        }


    
    # TODO: Define form fields here

    

class LoginForm(forms.Form):
    # TODO: Define form fields here
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'type': 'text',
        'placeholder': 'Nombre de usuario',
        }))
    password = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'type':'password',
        'placeholder':'Ingrese contraseña'
        }))

    def clean(self):
        user_found = User.objects.filter(username= self.cleaned_data['username']).exists()
        if not user_found:
            self.add_error('username','Username y/o Password no encontrados')
        else:
            user = User.objects.get(username = self.cleaned_data['username'])
            if not (user.check_password(self.cleaned_data['password'])):
                self.add_error('username','Username y/o Password no encontrados')
