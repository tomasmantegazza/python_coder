from django.urls import path
from AppCode import views
from AppCode.views import cursos

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('apicursoFormulario', views.apiCursoFormulario, name="apiCursoFormulario"),
    path('buscar', views.buscar, name="Buscar"),
    path('mostrar', views.mostrar, name="Mostrar"),
    path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario")

]

