from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Profesor, Atleta, Deporte, Otra_actividad
from .forms import ProfesorForm, AtletaForm, DeporteForm, Otra_actividadForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')

def about(request):
    return render(request, 'mi_primer_app/about.html')

@login_required
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_profesor = Profesor(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                edad=form.cleaned_data['edad'],
                deporte=form.cleaned_data['deporte'], 
            )
            nuevo_profesor.save()
            return redirect('inicio')
    else:
        form = ProfesorForm()  
        return render(request, "mi_primer_app/crear_profesor.html", {"form":form})

@login_required   
def crear_atleta(request):
    if request.method == 'POST':
        form = AtletaForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_atleta = Atleta(
                 nombre=form.cleaned_data['nombre'],
                 apellido=form.cleaned_data['apellido'],
                 email=form.cleaned_data['email'],
                 edad=form.cleaned_data['edad'],
                 deporte=form.cleaned_data['deporte'],
                 fecha_inscripcion=form.cleaned_data['fecha_inscripcion'],     
            )
            nuevo_atleta.save()
            return redirect('inicio')
    else:
        form = AtletaForm()  
        return render(request, "mi_primer_app/crear_atleta.html", {"form":form})

@login_required
def crear_deporte(request):
    if request.method == 'POST':
        form = DeporteForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_deporte = Deporte(
                nombre=form.cleaned_data['nombre'],
                profesor=form.cleaned_data['profesor'],
                dias=form.cleaned_data['dias'],
                horarios=form.cleaned_data['horarios'],                
            )
            nuevo_deporte.save()
            return redirect('inicio')
    else:
        form = DeporteForm()  
        return render(request, "mi_primer_app/crear_deporte.html", {"form":form})
    
def deportes(request):
    deportes = Deporte.objects.all()
    return render(request, 'mi_primer_app/deportes.html', {'deportes': deportes})

def buscar_deportes(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        deportes = Deporte.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/deportes.html', {'deportes': deportes, 'nombre': nombre})

# Aca vamos a ver ejemplos de Vistas Basadas en Clases
class ProfesorListView(ListView):
     model = Profesor
     template_name = 'mi_primer_app/listar_profesores.html' 
     context_object_name = 'profesores'

class AtletaListView(ListView):
     model = Atleta
     template_name = 'mi_primer_app/listar_atletas.html' 
     context_object_name = 'atletas'

class Otra_actividadListView(ListView):
     model = Otra_actividad
     template_name = 'mi_primer_app/listar_otras_actividades.html' 
     context_object_name = 'otras_actividades' 

class Otra_actividadCreateView(LoginRequiredMixin, CreateView):
     model = Otra_actividad
     form_class = Otra_actividadForm
     template_name = 'mi_primer_app/crear_otra_actividad.html'
     success_url = reverse_lazy('listar-otras-actividades')

class Otra_actividadDetailView(DetailView):
     model = Otra_actividad
     template_name = 'mi_primer_app/detalle_otra_actividad.html'
     context_object_name = 'otra_actividad'

class AtletaDetailView(DetailView):
     model = Atleta
     template_name = 'mi_primer_app/detalle_atleta.html'
     context_object_name = 'atleta'

class ProfesorDetailView(DetailView):
     model = Profesor
     template_name = 'mi_primer_app/detalle_profesor.html'
     context_object_name = 'profesor'

class Otra_actividadUpdateView(LoginRequiredMixin, UpdateView):
     model = Otra_actividad
     form_class = Otra_actividadForm
     template_name = 'mi_primer_app/crear_otra_actividad.html'
     success_url = reverse_lazy('listar-otras-actividades')

class ProfesorUpdateView(LoginRequiredMixin, UpdateView):
     model = Profesor
     form_class = ProfesorForm
     template_name = 'mi_primer_app/crear_profesor.html'
     success_url = reverse_lazy('listar-profesores')
    
class AtletaUpdateView(LoginRequiredMixin, UpdateView):
     model = Atleta
     form_class = AtletaForm
     template_name = 'mi_primer_app/crear_atleta.html'
     success_url = reverse_lazy('listar-atletas')

class Otra_actividadDeleteView(LoginRequiredMixin, DeleteView):
     model = Otra_actividad
     template_name = 'mi_primer_app/eliminar_otra_actividad.html'
     success_url = reverse_lazy('listar-otras-actividades')

class ProfesorDeleteView(LoginRequiredMixin, DeleteView):
     model = Profesor
     template_name = 'mi_primer_app/eliminar_profesor.html'
     success_url = reverse_lazy('listar-profesores')

class AtletaDeleteView(LoginRequiredMixin, DeleteView):
     model = Atleta
     template_name = 'mi_primer_app/eliminar_atleta.html'
     success_url = reverse_lazy('listar-atletas')