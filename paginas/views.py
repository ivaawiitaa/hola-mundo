
# Create your views here.
from django.http import HttpResponse

#Agregar pagina de inicio
def vista_inicio(request):
    return HttpResponse("Hello, World!")
#Agregar pagina acercade
def vista_acerca_de(request):
    return HttpResponse("Pagina acerca de")