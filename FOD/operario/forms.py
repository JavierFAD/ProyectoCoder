from django import forms


class BuscaOperario(forms.Form):
    apellido = forms.CharField(required=False)
    legajo = forms.IntegerField(initial=8)

