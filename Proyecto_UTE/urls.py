"""Proyecto_UTE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from appUno.views import home, RegistrarContacto_view,  EliminarContacto_view, EditarContacto_view, EditarContactos_view, homenotas, RegistrarNotas_view, EliminarNota_view, EditarNotas_view, EditarNota_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('',home, name='contact'),
    path('RegistrarContacto/', RegistrarContacto_view),
    path('EliminarContacto/<id_contacto>',  EliminarContacto_view),
    path('EditarContactos/<cedula>', EditarContactos_view),
    path('EditarContacto/', EditarContacto_view),

    path('Notas/<id_contacto>',homenotas, name='notas'),
    path('RegistrarNotas/<id_contacto>', RegistrarNotas_view),
    path('EliminarNota/<id_apunte>', EliminarNota_view),
    path('EditarNotas/<nombre>', EditarNotas_view),
    path('EditarNota/', EditarNota_view),
    ]  
