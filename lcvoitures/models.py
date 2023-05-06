from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib import admin
import datetime


# Create your models here.
from core import settings


class employe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='employee',null=True)
    salaire = models.FloatField(max_length=2, null=False)
    date_embauche = models.DateField(default=datetime.date.today())
    situation = models.CharField(max_length=10,default="en cours")

    def __str__(self):
        return str(self.user)


class client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name= 'client',null=True)
    point = models.IntegerField(default=0)
    telephone = PhoneNumberField()
    def __str__(self):
        return str(self.user)


class type_voiture(models.Model):
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.type


class marque(models.Model):
    marque = models.CharField(max_length=20)
    def __str__(self):
        return self.marque


class voiture(models.Model):
    immatriculation = models.CharField(max_length=10, primary_key=True)
    model = models.CharField(max_length=10)
    couleur = models.CharField(max_length=10)
    type_voiture = models.ForeignKey(type_voiture, on_delete=models.CASCADE)
    marque = models.ForeignKey(marque, on_delete=models.CASCADE)
    dispo = models.BooleanField(default=True)
    prix_journalier = models.FloatField()
    description = models.CharField(max_length=200)
    type_carburant=models.CharField(max_length=10,default="Gasoil")
    etat_carburant=models.FloatField(default=0)

    def __str__(self):
        return str(self.model) + str(self.marque)


class photo_image(models.Model):
    voiture = models.ForeignKey(voiture, on_delete=models.CASCADE,)
    image = models.ImageField(max_length=200)

    def __str__(self):
        return str(self.voiture)+ " " + str(self.id)


class reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    voiture = models.ForeignKey(voiture, on_delete=models.CASCADE, related_name='voiture')
    dateDebut = models.DateTimeField()
    dateFin = models.DateTimeField()
    remaqrques = models.CharField(max_length=200)
    etat = models.CharField(max_length=20,default="En cours")
    ditance_parcourut = models.FloatField(max_length=2,default=0)


admin.site.register(client)
admin.site.register(employe)
admin.site.register(type_voiture)
admin.site.register(marque)
admin.site.register(voiture)
admin.site.register(reservation)
admin.site.register(photo_image)
