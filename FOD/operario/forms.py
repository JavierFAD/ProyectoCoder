from django import forms


class BuscaOperario(forms.Form):
    apellido = forms.CharField()