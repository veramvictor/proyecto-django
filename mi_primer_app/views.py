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

from django.shortcuts import get_object_or_404

@login_required
def editar_deporte(request, pk):
    deporte = get_object_or_404(Deporte, pk=pk)  # Obtiene el deporte o lanza un 404 si no existe
    if request.method == 'POST':
        form = DeporteForm(request.POST)
        if form.is_valid():
            # Actualiza los datos del deporte
            deporte.nombre = form.cleaned_data['nombre']
            deporte.profesor = form.cleaned_data['profesor']
            deporte.dias = form.cleaned_data['dias']
            deporte.horarios = form.cleaned_data['horarios']
            deporte.save()
            return redirect('deportes')  # Redirige a la lista de deportes
    else:
        # Prellena el formulario con los datos existentes
        form = DeporteForm(initial={
            'nombre': deporte.nombre,
            'profesor': deporte.profesor,
            'dias': deporte.dias,
            'horarios': deporte.horarios,
        })
    return render(request, 'mi_primer_app/editar_deporte.html', {'form': form, 'deporte': deporte})

@login_required
def editar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)  
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.edad = form.cleaned_data['edad']
            profesor.deporte = form.cleaned_data['deporte']
            profesor.save()
            return redirect('listar-profesores')  
    else:
        form = ProfesorForm(initial={
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'edad': profesor.edad,
            'deporte': profesor.deporte,
        })
    return render(request, 'mi_primer_app/editar_profesor.html', {'form': form, 'profesor': profesor})

@login_required
def editar_atleta(request, pk):
    atleta = get_object_or_404(Atleta, pk=pk)  
    if request.method == 'POST':
        form = AtletaForm(request.POST)
        if form.is_valid():
            atleta.nombre = form.cleaned_data['nombre']
            atleta.apellido = form.cleaned_data['apellido']
            atleta.edad = form.cleaned_data['edad']
            atleta.email = form.cleaned_data['email']
            atleta.deporte = form.cleaned_data['deporte']
            atleta.fecha_inscripcion = form.cleaned_data['fecha_inscripcion']            
            atleta.save()
            return redirect('listar-atletas')  
    else:
        form = AtletaForm(initial={
            'nombre': atleta.nombre,
            'apellido': atleta.apellido,
            'edad': atleta.edad,
            'email': atleta.email,
            'deporte': atleta.deporte,
            'fecha_inscripcion': atleta.fecha_inscripcion,
        })
    return render(request, 'mi_primer_app/editar_atleta.html', {'form': form, 'atleta': atleta})


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

class DeporteDetailView(DetailView):
     model = Deporte
     template_name = 'mi_primer_app/detalle_deporte.html'
     context_object_name = 'deportes'

class Otra_actividadUpdateView(LoginRequiredMixin, UpdateView):
     model = Otra_actividad
     form_class = Otra_actividadForm
     template_name = 'mi_primer_app/crear_otra_actividad.html'
     success_url = reverse_lazy('listar-otras-actividades')

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

class DeporteDeleteView(LoginRequiredMixin, DeleteView):
     model = Deporte
     template_name = 'mi_primer_app/eliminar_deporte.html'
     success_url = reverse_lazy('deportes')