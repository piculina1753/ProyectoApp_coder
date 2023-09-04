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
    return render(req, "lista_curso.html", {"lista_cursos": lista})

# def probando_template(request):
# #     miHtml = open(r"C:\Users\Nadia\Documents\Curso python\proyectocoder\AppCoder\templates\lista_cursos.html")
# #     plantilla = Template(miHtml.read())
# #     miHtml.close()
    
# #     miContexto = Context({"my_name": "Nadia", "notas": [5,1,8,9,2]})
    
# #     documento = plantilla.render(miContexto)
# #     return HttpResponse(documento)

#  plantilla = loader.get_template ("templates1.html")
#  documento = plantilla.render({"my_name": "Nadia", "notas": [5,1,8,9,2,7]})
#  return HttpResponse(documento)