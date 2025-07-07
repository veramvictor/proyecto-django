from django.urls import path
from .views import inicio, crear_profesor, crear_atleta, crear_deporte, deportes, buscar_deportes

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('crear-profesor/', crear_profesor, name='crear-profesor'),
    path('crear-atleta/', crear_atleta, name='crear-atleta'),
    path('crear-deporte/', crear_deporte, name='crear-deporte'),   
    path('deportes/', deportes, name='deportes'),
    path('deportes/buscar', buscar_deportes, name='buscar-deportes'),
]