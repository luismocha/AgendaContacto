from django.contrib import admin
from .models import Contacto
from .models import Apunte


class AdminContacto(admin.ModelAdmin):
    list_display = ["id_contacto", "nombres",
                    "apellidos", "email", "cedula", "celular"]

    class Meta(object):
        model = Contacto


admin.site.register(Contacto, AdminContacto)


class AdminApunte(admin.ModelAdmin):
    list_display = ["__str__", "id_contacto",
                    "id_apunte", "nombre", "contenido"]

    class Meta(object):
        model = Apunte


admin.site.register(Apunte, AdminApunte)
