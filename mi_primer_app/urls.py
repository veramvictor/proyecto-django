from django.urls import path
from .views import (inicio, crear_profesor, crear_atleta, crear_deporte, deportes, buscar_deportes, about, 
                    editar_deporte, editar_profesor, editar_atleta,                    Otra_actividadCreateView, Otra_actividadListView, Otra_actividadDeleteView, Otra_actividadDetailView,
                    Otra_actividadUpdateView, AtletaListView, ProfesorListView, AtletaDetailView, ProfesorDetailView,
                    ProfesorDeleteView, AtletaDeleteView, DeporteDetailView, DeporteDeleteView)


urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('crear-profesor/', crear_profesor, name='crear-profesor'),
    path('crear-atleta/', crear_atleta, name='crear-atleta'),
    path('crear-deporte/', crear_deporte, name='crear-deporte'),   
    path('deportes/', deportes, name='deportes'),
    path('deportes/buscar', buscar_deportes, name='buscar-deportes'),
    path('editar-deporte/<int:pk>/', editar_deporte, name='editar-deporte'),
    path('editar-profesor/<int:pk>/', editar_profesor, name='editar-profesor'),
    path('editar-atleta/<int:pk>/', editar_atleta, name='editar-atleta'),
    path('about/', about, name='about'),
    
    
    # urls con Vistas Basadas en Clases
    path('detalle-deporte/<int:pk>', DeporteDetailView.as_view(), name='detalle-deporte'),
    path('listar-profesores/', ProfesorListView.as_view(), name='listar-profesores'), 
    path('listar-atletas/', AtletaListView.as_view(), name='listar-atletas'), 
    path('listar-otras-actividades/', Otra_actividadListView.as_view(), name='listar-otras-actividades'), 
    path('crear-otra-actividad/', Otra_actividadCreateView.as_view(), name='crear-otra-actividad'), 
    path('detalle-otra-actividad/<int:pk>', Otra_actividadDetailView.as_view(), name='detalle-otra-actividad'),
    path('detalle-profesor/<int:pk>', ProfesorDetailView.as_view(), name='detalle-profesor'),
    path('detalle-atleta/<int:pk>', AtletaDetailView.as_view(), name='detalle-atleta'),
    path('editar/<int:pk>/', Otra_actividadUpdateView.as_view(), name='editar-otra-actividad'),
    path('eliminar/<int:pk>/', Otra_actividadDeleteView.as_view(), name='eliminar-otra-actividad'),
    path('eliminar-profesor/<int:pk>/', ProfesorDeleteView.as_view(), name='eliminar-profesor'),
    path('eliminar-atleta/<int:pk>/', AtletaDeleteView.as_view(), name='eliminar-atleta'),
    path('eliminar-deporte/<int:pk>/', DeporteDeleteView.as_view(), name='eliminar-deporte'),
]
