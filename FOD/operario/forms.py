from django import forms


class BuscaOperario(forms.Form):
    apellido = forms.CharField()
    
class BuscaLegajo(forms.Form):
    legajo = forms.IntegerField()
