from django.urls import path

from .views import buscar, busqueda_camada, curso, cursoFormulario, cursos, entregables, estudiantes, inicio, lista_curso, profesores


urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('', inicio),
    path('lista-cursos/', lista_curso),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
    path('cursoFormulario/', cursoFormulario, name="CursoFormulario"),
    path('busqueda_camada/', busqueda_camada, name="busqueda_camada"),
    path('buscar/', buscar, name="buscar"),
]
