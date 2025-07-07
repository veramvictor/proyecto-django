from django.contrib import admin

# Register your models here.
from .models import Profesor, Atleta, Deporte

register_models = [Profesor, Atleta, Deporte]

admin.site.register(register_models)