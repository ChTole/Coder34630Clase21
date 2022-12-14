from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CursoFormulario
from .models import Curso

# Create your views here.

def curso(request, camada, nombre):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado! </p>
    """)


def lista_curso(request):

    lista = Curso.objects.all()

    return render(request, "lista_cursos.html", {"lista_cursos": lista})


def inicio(request):
    
    return render(request, "inicio.html")

def cursos(request):

    lista = Curso.objects.all() 

    return render(request, "cursos.html", {"lista_cursos": lista})

def profesores(request):
    
    return render(request, "profesores.html")

def estudiantes(request):
    
    return render(request, "estudiantes.html")

def entregables(request):
    
    return render(request, "estudiantes.html")


def cursoFormulario(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            curso = Curso(nombre=data['curso'], camada=data['camada'])
            curso.save()
            return redirect('Cursos')
            # return render(request, 'inicio.html')
    else:
        mi_formulario = CursoFormulario()
    
    
    return render(request, "cursoFormulario.html", {'mi_formulario': mi_formulario})

def busqueda_camada(request):
    
    return render(request, 'busqueda_camada.html')

def buscar(request):
    
    camada_buscada = request.GET['camada']
    
    curso = Curso.objects.get(camada = camada_buscada)
    
    return render(request, 'resultadoBusqueda.html', {'curso': curso, 'camada': camada_buscada})