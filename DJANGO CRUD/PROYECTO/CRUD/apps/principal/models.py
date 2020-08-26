from django.db import models

# Si hacemos Cambios aqui toca volver a ejecutar Manage.py makemigrations y migrate
class Ciudad(models.Model):
     idCiudad = models.AutoField(primary_key=True)
     nombre = models.CharField(max_length=100,null=True)
     descripcion=models.CharField(max_length=100,null=True)

     def __str__(self):
         return self.nombre

class TipoDocumento(models.Model):
     idTipoDocumento = models.AutoField(primary_key=True)
     nombre = models.CharField(max_length=100,null=True)
     descripcion=models.CharField(max_length=100,null=True)

     def __str__(self):
         return self.nombre

class Persona(models.Model):
     idPersona = models.AutoField(primary_key=True)
     nombres = models.CharField(max_length=100,null=True)
     apellidos = models.CharField(max_length=120, null=True)
     idTipoDocumento = models.ForeignKey(TipoDocumento,db_column='idTipoDocumento',on_delete=models.RESTRICT,null=True)
     documento = models.CharField(max_length=10,null=True)
     lugarResidencia = models.ForeignKey(Ciudad, db_column='idCiudad' ,blank=True, on_delete=models.RESTRICT,null=True)
     fechaNacimiento = models.DateField(null=True)
     email = models.EmailField(max_length=100,null=True)
     telefono =models.CharField(max_length=20,null=True)
     usuario=models.CharField(max_length=30,null=True)
     password=models.CharField(max_length=20,null=True)



     def __str__(self):
         return self.nombre

         