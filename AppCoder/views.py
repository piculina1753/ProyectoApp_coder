from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from django.template import Template, Context
from django.template import loader


# Create your views here.
def curso(req, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    
    return HttpResponse (f"""
    <p>Curso: {curso.nombre} - Camada: {curso.camada} creado con exito!<p/>
    """)

def lista_cursos(req):
    lista = Curso.objects.all()
    return render(req, "lista_cursos.html", {"lista_cursos": lista})

def inicio(req):
    return render(req,"inicio.html")

def cursos(req):
    return render(req,"cursos.html")

def profesores(req):
   return render(req,"profesores.html")

def estudiantes(req):
  return render(req,"estudiantes.html")

def entregables(req):
    return render(req,"entregables.html")