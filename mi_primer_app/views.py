from django.shortcuts import render, redirect
from .models import Profesor, Atleta, Deporte
from .forms import ProfesorForm, AtletaForm, DeporteForm

# Create your views here.
from django.http import HttpResponse
def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')

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
