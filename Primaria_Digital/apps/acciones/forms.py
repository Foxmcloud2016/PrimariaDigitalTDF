from django import forms
from .models import Accion
from datetime import datetime

class AccionForm(forms.ModelForm):
    class Meta:
        model = Accion
        fields = ('escuela','accion','fecha',)
        widgets = {
        'escuela': forms.Select(attrs={
            'type':'textarea',
            }),
        'accion': forms.Textarea(attrs={
            'type':'textarea',
            'rows':'4',
             'cols':'50',
            }),
        }

    def clean(self,**kwargs):
        data = super(AccionForm,self).clean(**kwargs)
        return data
