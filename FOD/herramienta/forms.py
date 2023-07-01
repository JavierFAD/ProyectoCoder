from django import forms

class BuscaHerramienta(forms.Form):
    rastreo = forms.IntegerField()
    