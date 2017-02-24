from django import forms
# Traemos modelo Dispositivo y Adm
from .models import Dispositivo, Adm

"""
CHOICES_ESTADO = (
    (1, 'Buen Estado'),
    (2, 'Esperando Servicio Tecnico'),
    (3, 'Roto'),
)
"""

class DispositivoUnicoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ('adm', 'estado', 'tipo', 'n_m', 'marca', 'modelo', 'n_s')
        widgets = {
            'adm': forms.TextInput(attrs={
                'type': 'hidden'
            }),
            'tipo': forms.TextInput(attrs={
                'type': 'hidden'
            }),
            'n_m': forms.TextInput(attrs={
                'type': 'hidden'
            }),
            'estado': forms.TextInput(attrs={
                'type': 'hidden'
            }),
        }

    def clean_n_m(self):
        adm = self.cleaned_data['adm']
        n_m = self.cleaned_data['n_m']
        if Dispositivo.objects.filter(adm=adm, n_m=n_m).exists():
            raise forms.ValidationError(
                'El numero de maquina ingresado ya existe en el adm')
        else:
            return n_m


class NetbookForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ('adm', 'estado', 'tipo', 'n_m', 'marca', 'modelo', 'n_s')
        widgets = {
            'adm': forms.TextInput(attrs={
                'type': 'hidden'
            }),
            'tipo': forms.TextInput(attrs={
                'type': 'hidden'
            }),
            'estado': forms.TextInput(attrs={
                'type': 'hidden'
            }),
        }

    def clean_n_m(self):
        adm = self.cleaned_data['adm']
        n_m = self.cleaned_data['n_m']
        # Si existe un numero de m duplicado
        if Dispositivo.objects.filter(adm=adm, n_m=n_m).exists():
            raise forms.ValidationError(
                'El numero de maquina ingresado ya existe en el adm')
        else:
            return n_m


"""
from collections import Counter
class NetbookMasiveForm(forms.Form):
    adm = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    maquina1 = forms.CharField(max_length=40)
    maquina2 = forms.CharField(max_length=40)
    maquina3 = forms.CharField(max_length=40)
    maquina4 = forms.CharField(max_length=40)
    maquina5 = forms.CharField(max_length=40)
    maquina6 = forms.CharField(max_length=40)
    maquina7 = forms.CharField(max_length=40)
    maquina8 = forms.CharField(max_length=40)
    maquina9 = forms.CharField(max_length=40)
    maquina10 = forms.CharField(max_length=40)
    maquina11 = forms.CharField(max_length=40)
    maquina12 = forms.CharField(max_length=40)
    maquina13 = forms.CharField(max_length=40)
    maquina14 = forms.CharField(max_length=40)
    maquina15 = forms.CharField(max_length=40)
    maquina16 = forms.CharField(max_length=40)
    maquina17 = forms.CharField(max_length=40)
    maquina18 = forms.CharField(max_length=40)
    maquina19 = forms.CharField(max_length=40)
    maquina20 = forms.CharField(max_length=40)
    maquina21 = forms.CharField(max_length=40)
    maquina22 = forms.CharField(max_length=40)
    maquina23 = forms.CharField(max_length=40)
    maquina24 = forms.CharField(max_length=40)
    maquina25 = forms.CharField(max_length=40)
    maquina26 = forms.CharField(max_length=40)
    maquina27 = forms.CharField(max_length=40)
    maquina28 = forms.CharField(max_length=40)
    maquina29 = forms.CharField(max_length=40)
    maquina30 = forms.CharField(max_length=40)

    def clean(self):
        adm = self.cleaned_data['adm']
        data = self.cleaned_data  # Traigo todos los datos
        maquinas = [] # en esta lista guardo los numeros de serie de las maquinas
        for maquina in data.values():
            maquinas.append(maquina)  # Guardando maquinas
        # Si existen duplicados se agrega al valor k y luego
        duplicado = [k for k, v in Counter(maquinas).items() if v > 1]
        # a la variable duplicado
        if duplicado == []:  # si existe duplicado
            for maquina in maquinas:
                if Dispositivo.objects.filter(adm=adm, n_s=maquina).exists():
                    raise forms.ValidationError(
                        'El numero de serie ingresado ya existe en la BD')
                else:
                    return self.cleaned_data
        else:
            raise forms.ValidationError('Numero de serie ingresado duplicado')
"""
