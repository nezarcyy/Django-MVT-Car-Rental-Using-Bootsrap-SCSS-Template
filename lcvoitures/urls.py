from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls import include
from .views import *
from . import views
from django.urls import path, re_path
from apps.home import views
from lcvoitures.views import *
urlpatterns = [

    path('', homeInex),
    path('voitures',TousLesvoitures,name="voitures"),
    path('employés',indexEmploye,name='employesIndex'),
    path('clients',indexClient,name='clientIndex'),
    # path('home/index.html',views.totalrevenu, name = 'totalrevenu'),
    # path('home/index.html',views.indexClientDash, name = 'indexClientDash'),
    path('home/index.html',dashboard, name = 'dashboard'),
    path('reservations', indexReservation , name='indexReservations'),
    path('chercherVoiture',chercherVoiture,name='chercher'),
    path("login/", LogoutView.as_view(), name="logout"),
    path('AjouterVoiture',AjouterVoiture,name="ajouterVoiture",),
    path('AjouterClient',AjouterClient,name="ajouterClient"),
    path('detailsVoiture/<str:immatriculation>',DetailVoiture,name="detaille"),
    path('ajouterEmploye',ajouterEmploye,name="ajouterEmploye"),
    path('modifiercompte',modifierCompte,name="modfiercompte"),
    path('modifierEmp/<int:id>',modifierEmploye,name="modifierEmploye"),
    path('modfierClient/<int:id>', mdifierClient, name="modfierClient"),
    path('modifierVoiture/<str:immatriculation>',modifierVoiture,name = "modifierVoiture"),
    path('supprimerVoiture/<str:immatriculation>',supprimer_voiture,name="supprimerVoiture"),
    path('supprimerClient/<int:id>',supprimer_client,name="supperimerClient"),
    path('supprimetEmploye/<int:id>',supprimer_employe,name="supprimerEmploye"),
    path('mesReservations',mesReservations,name="mesRes"),
    path('AjouterReservation/<str:immatriculation>/<str:dateDebut>/<str:dateFin>/',ajouterReservation,name="Reservervoiture"),
    re_path(r'^.*\.*', views.pages, name='pages'),

]