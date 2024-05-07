from django import forms
from django.core.exceptions import ValidationError
from .models import Proveedor, Producto

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if len(str(dni)) > 8:
            raise ValidationError('El DNI ingresado no es valido.')
        return dni


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_actual': forms.TextInput(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'})
        }
