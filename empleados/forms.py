# empleados/forms.py
from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'email', 'telefono', 'direccion', 'fecha_contratacion', 'puesto', 'salario_base']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
            'salario_base': forms.NumberInput(attrs={'step': '0.01'}),
        }
