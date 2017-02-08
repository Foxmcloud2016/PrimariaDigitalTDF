from django import forms
from .models import Dispositivo,Adm

CHOICES_ESTADO = (
    (1,'Buen Estado'),
    (2,'Esperando Servicio Tecnico'),
    (3,'Roto'),
    )

class DispositivoUnicoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ('adm','estado','tipo','n_m','marca','modelo','n_s')
        widgets = {
        'adm' : forms.TextInput(attrs = {
            'type': 'hidden'
            }),
        'tipo': forms.TextInput(attrs = {
            'type': 'hidden'
            }),
        'n_m': forms.TextInput(attrs = {
            'type': 'hidden'
            }),
        'estado' : forms.RadioSelect(choices = CHOICES_ESTADO),
        }

    def clean_n_m(self):
        adm = self.cleaned_data['adm']
        n_m = self.cleaned_data['n_m']
        if Dispositivo.objects.filter(adm = adm, n_m = n_m).exists():
            raise forms.ValidationError('El numero de maquina ingresado ya existe en el adm') 
        else:
            return n_m

class NetbooksForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ('adm','estado','tipo','n_m','marca','modelo','n_s')
        widgets = {
        'adm' : forms.TextInput(attrs = {
            'type': 'hidden',
            }),
        'tipo': forms.TextInput(attrs = {
            'type': 'hidden',
            }),
        'estado' : forms.TextInput(attrs = {
            'type': 'hidden',
            'value': '1',
            }),
        'marca': forms.TextInput(attrs = {
            'type': 'hidden',
            }),
        'modelo': forms.TextInput(attrs = {
            'type': 'hidden',
            }),
        'n_m': forms.TextInput(attrs = {
            'type': 'hidden',
            'value': '1',
            }),
        'n_s': forms.TextInput(attrs ={
            'label': 'Numero de Serie',
            }),
        }
