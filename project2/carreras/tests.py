import pytest
from carreras.repository import CarreraRepository
from carreras.models import Carrera
from carreras.factories import CarreraFactory
def test_compare_parameters():
    a = 10 
    b = 15
    c = a + b
    assert c == 25

@pytest.mark.django_db
def test_get_carreras():
    carrera_nueva = Carrera.objects.create(nombre="Ingenieria en Sistemas", duracion=2)

    repository = CarreraRepository()
    carreras = repository.get_all_carerras()

    assert carreras.count() == 1

@pytest.mark.django_db
def test_create_carrera():
    nombre = "Ingenieria en Sistemas"
    duracion = 2

    repository = CarreraRepository()

    carrera = repository.create_carrera(nombre, duracion)

    assert carrera.nombre == nombre



@pytest.mark.django_db
def test_get_carrera():

    carrera = CarreraFactory()
    carrera.save()
    repository = CarreraRepository()
    carreras = repository.get_all_carerras()

    assert carreras.count()== 2