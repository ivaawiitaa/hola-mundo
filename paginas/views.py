
# Create your views here.
from django.http import HttpResponse


def vista_inicio(request):
    return HttpResponse("Hello, World!")

def vista_acerca_de(request):
    return HttpResponse("Pagina acerca de")