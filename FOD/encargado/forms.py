from django import forms

class BuscaEncargado(forms.Form):
    apellido = forms.CharField(required=False)
    legajo = forms.IntegerField(initial=8)
