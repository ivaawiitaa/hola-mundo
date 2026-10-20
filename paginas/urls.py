from django.urls import path

from .views import vista_inicio
from .views import vista_acerca_de

#Asociar las urls
urlpatterns = [
    path("", vista_inicio),
    path("acerca-de/", vista_acerca_de),
]

