from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def familiares(self):
    return HttpResponse("Estos son mis familiares: ")

def templateFamilia(self):
    
    diccionario = {
        "nombre": "Tomas",
        "apellido": "Mantegazza",
        "hobbie": "Autos"
    }
    
    plantilla = loader.get_template('template.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)
    

