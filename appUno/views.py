#from django.http import HttpResponse
from django.shortcuts import render
from .models import Contacto
from django.shortcuts import redirect
from django.contrib import messages

from .models import Apunte
# Create your views here.


def home(request):
    contacto = Contacto.objects.all()
    return render(request, "contact.html", {"contacto": contacto})


def RegistrarContacto_view(request):
    nombres = request.POST['txtnombres']
    apellidos = request.POST['txtapellidos']
    cedula = request.POST['txtcedula']
    celular = request.POST['txtcelular']
    email = request.POST['txtemail']

    contacto = Contacto.objects.create(nombres=nombres, apellidos=apellidos, cedula=cedula, celular=celular, email=email)
    messages.success(request, '¡Contacto Registrado!')
    return redirect('/')


def EditarContactos_view(request, cedula):
    contacto = Contacto.objects.get(cedula=cedula)
    return render(request, "EditarContact.html", {"contacto": contacto})


def EditarContacto_view(request):
    nombres = request.POST['txtnombres']
    apellidos = request.POST['txtapellidos']
    cedula = request.POST['txtcedula']
    celular = request.POST['txtcelular']
    email = request.POST['txtemail']
    contacto = Contacto.objects.get(cedula=cedula)
    contacto.nombres = nombres
    contacto.apellidos = apellidos
    contacto.cedula = cedula
    contacto.celular = celular
    contacto.email = email
    contacto.save()
    messages.success(request, '¡Contacto actualizado!')
    return redirect('/')


def EliminarContacto_view(request, id_contacto):
    contacto = Contacto.objects.get(id_contacto=id_contacto)
    contacto.delete()

    messages.success(request, '¡Contacto  eliminado!')

    return redirect('/')


def homenotas(request, id_contacto):
    nom_con = Contacto.objects.filter(pk=id_contacto)
    ide_con = Contacto.objects.get(id_contacto=id_contacto)
    apunte = Apunte.objects.filter(id_contacto=id_contacto)
    ctx = {'nom_con': nom_con, 'apunte': apunte}
    return render(request, "notas.html", ctx)


def RegistrarNotas_view(request, id_contacto):
    id_contacto = Contacto.objects.get(id_contacto=id_contacto)    
    nombre = request.POST['txtnombre']
    contenido = request.POST['txtcontenido']
    apunte = Apunte.objects.create(id_contacto=id_contacto, nombre=nombre, contenido=contenido)
    messages.success(request, '¡Nota Registrada!')    
    return redirect("/")


def EliminarNota_view(request, id_apunte):
    apunte = Apunte.objects.get(id_apunte=id_apunte)
    apunte.delete()
    messages.success(request, '¡Nota  eliminado!')
    #return redirect('/')
    return redirect("/")

def EditarNotas_view(request, nombre):
    apunte = Apunte.objects.get(nombre=nombre)
    return render(request, "EditarNota.html", {"apunte": apunte})


def EditarNota_view(request):
    nombre = request.POST['txtnombre']
    contenido = request.POST['txtcontenido']
    apunte = Apunte.objects.get(nombre=nombre)
    apunte.nombre = nombre
    apunte.contenido = contenido
    apunte.save()
    messages.success(request, '¡Nota actualizado!')
    return redirect("/")

