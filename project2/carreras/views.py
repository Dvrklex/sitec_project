from django.shortcuts import HttpResponse,render
# Create your views here.
from carreras.models import Carrera,Materia
from carreras.repository import CarreraRepository

def index(request):
    return HttpResponse('Este es el index')

def carrera_view(request):
    view_name = 'Carreras'
    repository = CarreraRepository()
    carreras = repository.get_all_carerras()
    return render(request,'carreras\index_carreras.html', {'view_name':view_name, 'carreras':carreras}) 

def materia_view(request):
    return HttpResponse('URl Materia')


