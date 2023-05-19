from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.carrera_view, name='Carrera'),
    path('materia', views.materia_view, name='Materia'),
    
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 