# from django import forms

# class FormularioEditarConsumible(forms.Form):
    
#     designacion   = forms.CharField(max_length=50, required=False)
#     descripcion   = forms.CharField(max_length=200, label='Descripción breve del Producto', required=False)
#     cantidad      = forms.IntegerField(label='Ingrese la cantidad del producto',initial=1)
#     unidad        = forms.CharField(label='Ingrese la unidad(Ej: Kg, m, Lts)', required=False)
#     vencimiento   = forms.DateField(label='Formato mm/dd/aaaa', required=False)
#     lote          = forms.CharField(max_length=30, required=False)
#     especificacion= forms.TextInput()
#     imagen        = forms.ImageField(required=False)