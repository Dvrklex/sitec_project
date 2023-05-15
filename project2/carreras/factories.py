import factory 
from .models import Carrera


class CarreraFactory(factory.Factory):
    class Meta:
        model = Carrera

    nombre = "Ingenieria en Ingenieros"
    duracion = 2




    