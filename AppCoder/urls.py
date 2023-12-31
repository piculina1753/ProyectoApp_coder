
from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path("agrega-curso/<nombre>/<camada>", curso),
    path("lista_cursos", lista_cursos),
    path("", inicio, name="Inicio"),
    path("cursos/", cursos, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiantes, name="Estudiantes"),
    path("entregables/", entregables, name="Entregables"),
]
