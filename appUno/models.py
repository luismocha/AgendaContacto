from django.db import models

class Contacto(models.Model):
    id_contacto=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=30,blank=True)
    apellidos=models.CharField(max_length=30)
    cedula=models.CharField(max_length=10)
    celular=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        texto="{0}"
        return texto.format(self.nombres)

class Apunte(models.Model):
    id_apunte=models.AutoField(primary_key=True)
    id_contacto=models.ForeignKey(Contacto, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30,blank=True)
    contenido=models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre


