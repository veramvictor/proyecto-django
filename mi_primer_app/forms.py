from django import forms
from .models import Otra_actividad

class ProfesorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    edad = forms.IntegerField(min_value=10, max_value=100)
    deporte = forms.CharField(label="Deporte", max_length=100)

class AtletaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField()
    edad = forms.IntegerField(min_value=10, max_value=100)
    deporte = forms.CharField(label="Deporte", max_length=100)
    fecha_inscripcion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    
class DeporteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    profesor = forms.CharField(label="Profesor", max_length=100)
    dias = forms.CharField(label="Días", max_length=100)
    horarios = forms.CharField(label="Horarios", max_length=100)

# Aca vamos a crear Forumlarios para Vistas Basadas en Clases.
class Otra_actividadForm(forms.ModelForm):
      class Meta:
           model = Otra_actividad
           fields = ['nombre', 'profesor']

