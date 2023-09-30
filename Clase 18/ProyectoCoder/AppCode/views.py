from django.shortcuts import render
from AppCode.models import *
from django.http import HttpResponse
from AppCode.forms import *


# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto = f"---> Curso: {curso.nombre}   Camada: {curso.camada}"
    
    
  #  return HttpResponse(documentoDeTexto)

def inicio(request):
    
    return render(request, 'AppCode/index.html')

def cursos(request):
    
    return render(request, 'AppCode/cursos.html')

def profesores(request):
    
    return render(request, 'AppCode/profesores.html')

def estudiantes(request):
    
    return render(request, 'AppCode/estudiantes.html')

def entregables(request):
    
    return render(request, 'AppCode/entregables.html')

def cursoFormulario(request):
    if request.method == 'POST':
        
        curso =  Curso(request.POST['curso'],(request.POST['camada']))
        curso.save()
        return render(request, "AppCode/index.html")
    
    return render(request, "AppCode/cursoFormulario.html")

def apiCursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso =  Curso(request.POST['curso'],(request.POST['camada']))
            curso.save()
            return render(request, "AppCode/index.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppCode/apiCursoFormulario.html", {"miFormulario": miFormulario})

def buscar(request):
    
    if request.method == 'POST':
        miFormulario = BuscaCursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cursos =  Curso.objects.filter(nombre__icontains=informacion["curso"])
            return render(request, "AppCode/lista.html", {"cursos": cursos})
        else:
            print("\n\nERROR IS_VALID FALSE\n\n")
    else:
        miFormulario= BuscaCursoFormulario()
    return render(request, "AppCode/apiCursoFormulario.html", {"miFormulario": miFormulario})

def mostrar(request):
    pass

def profesorFormulario(request):
    
    if request.method == 'POST':
        
        miFormulario = ProfesorFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            profesor =  Profesor(nombre=informacion["nombre"], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, "AppCode/index.html")
        
    else:
        miFormulario= ProfesorFormulario()
    return render(request, "AppCode/profesorFormulario.html", {"miFormulario": miFormulario})