from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Nombre: {self.first_name}, Apellido: {self.last_name}, Correo: {self.email_address}, Edad: {self.age}"

# COMANDOS

# from users_app.models import *
# Users.objects.all()
# Users.objects.create(first_name="Gustavo", last_name="Lopez",email_address="gustavo@correo.com", age=52)
# Users.objects.create(first_name="Rodrigo", last_name="Feliu",email_address="rodrigo@correo.com", age=39)
# Users.objects.create(first_name="Carlos", last_name="Rozas",email_address="carlos@correo.com", age=38)
# Users.objects.all()
# Users.objects.last() 
# Users.objects.first() 
# user_for_update = Users.objects.get(id=3)
# user_for_update.last_name="Pancakes"
# user_for_update.save()
# Users.objects.get(id=3)
# user_for_delete = Users.objects.get(id=2)
# user_for_delete.delete()
# Users.objects.all().order_by("first_name")
# Users.objects.all().order_by("-first_name")
