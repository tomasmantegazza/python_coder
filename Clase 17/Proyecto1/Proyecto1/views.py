from django.http import HttpResponse
from datetime import *
from django.template import Template, Context
from django.template import loader

def saludo(request):
	return HttpResponse("Que onda la bandaa")

def segunda_vista(request):
    return HttpResponse("Como estas")
    
def diaDeHoy(request):
    dia = datetime.now()
    documentoDeTexto = f"La fecha de hoy es:<br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto2 = f"Mi nombre es:<br> {nombre}"
    return HttpResponse(documentoDeTexto2)

def probandoTemplate(self):
    
    listaDeNotas = [2, 2, 3, 7, 2, 5]
    
    diccionario = {
        
        "first_name": "Tomas",
        "last_name": "Mantegazza",
        "hoy": datetime.now(),
        "notas": listaDeNotas
    }
    
    #Abrimos archivo HTML
    #miHtml = open(r"C:\Users\dobam\Desktop\PythonProyecto1\Proyecto1\Proyecto1\plantillas\template1.html")
    
    #Creamos el template usando la clase template
    #plantilla = Template(miHtml.read())
    
    #Cerramos el archivo abierto, ya que esta cargado en la variable plantilla
    #miHtml.close()
    
    #Creamos un contexto
    #miContexto = Context(diccionario)
    
    #Terminamos de contruir el template, renderizandolo con su contexto
    #documento = plantilla.render(miContexto)
    
    plantilla = loader.get_template('template1.html')
    
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
    