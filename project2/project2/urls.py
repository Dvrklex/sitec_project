from django.contrib import admin
from django.urls import path, include
from carreras.views import index

urlpatterns = [
    # path('', views.index , name='Index'),
    path('admin/', admin.site.urls),
    path('carreras/', include('carreras.urls')),
]

