from django.contrib import admin

# Register your models here.
from .models import Profesor, Atleta, Deporte, Otra_actividad

register_models = [Profesor, Atleta, Deporte, Otra_actividad]

admin.site.register(register_models)