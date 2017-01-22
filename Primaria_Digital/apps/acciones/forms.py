from django import forms
from .models import Accion
from datetime import datetime

class AccionForm(forms.ModelForm):
    class Meta:
        model = Accion
        fields = ('escuela','accion','fecha',)
        widgets = {
        'escuela': forms.Textarea(attrs={
            'type':'textarea',
            }),

        'accion': forms.Textarea(attrs={
            'type':'textarea',
            }),

        'fecha': forms.Textarea(attrs={
            'type':'date',
            }),
        }

    def clean(self,**kwargs):
        datos = self.cleaned_data
        print (datos['fecha'])

