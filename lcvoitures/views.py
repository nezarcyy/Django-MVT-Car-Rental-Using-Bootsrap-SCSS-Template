from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from lcvoitures.models import *
from lcvoitures.forms import *
from django.db import connection

# Create your views here.



def homeInex(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('home/index.html')
    else:
        return redirect('/chercherVoiture')

# Combined Views

@login_required()
def dashboard(request):
    # Fetch data from combined_view_1

    all = client.objects.raw("select * from lcvoitures_client left join auth_user on lcvoitures_client.user_id =auth_user.id")

    # Fetch data from combined_view_2

    with connection.cursor() as cursor:
        cursor.execute("SELECT SUM(lcvoitures_voiture.prix_journalier) AS totalrevenue FROM lcvoitures_voiture JOIN lcvoitures_reservation ON lcvoitures_voiture.immatriculation = lcvoitures_reservation.voiture_id")
        total_revenue = cursor.fetchone()[0] or 0 
        
    # Fetch data from combined_view_3

    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS totalreservations FROM lcvoitures_reservation")
        totalreservations = cursor.fetchone()[0] or 0 
        
    # Fetch data from combined_view_4

    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS totaldispo FROM lcvoitures_voiture WHERE lcvoitures_voiture.immatriculation NOT IN (SELECT lcvoitures_reservation.voiture_id FROM lcvoitures_reservation)")
        totaldispo = cursor.fetchone()[0] or 0 
    
    # Fetch data from combined_view_5

    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS potential FROM lcvoitures_client WHERE lcvoitures_client.id NOT IN (SELECT lcvoitures_reservation.user_id FROM lcvoitures_reservation)")
        potential = cursor.fetchone()[0] or 0 

    # Fetch data from combined_view_6
    employes=employe.objects.raw("SELECT * from lcvoitures_employe left join auth_user on lcvoitures_employe.user_id = auth_user.id")

    # Return Statement
    return render(request, 'home/index.html', {'utilisateurs': all, 'total_revenue': total_revenue,'totalreservations': totalreservations, 'totaldispo' : totaldispo, 'employees': employes, 'potential' : potential})

# End of Combined Views

def mesReservations(request):
    reservations =reservation.objects.filter(user_id=request.user.id ).select_related('user','voiture')
    if reservations is not None:
        return render(request,'reservation/reservationsFiltred.html',{"reservations": reservations })
    else:
        return render(request,'voitures/index.html')
    
@login_required()
def combined_view(request):
    all = client.objects.raw("select * from lcvoitures_client left join auth_user on lcvoitures_client.user_id =auth_user.id")
    return render(request, 'home/index.html', {'utilisateurs': all})



@login_required()
def TousLesvoitures(request):
    voitures = voiture.objects.all()
    return render(request, 'voitures/index.html', {'voitures': voitures})

@login_required()
def indexEmploye(request):

    employes=employe.objects.raw("SELECT * from lcvoitures_employe left join auth_user on lcvoitures_employe.user_id = auth_user.id")

    return render(request, 'employe/index.html', {'employees': employes})

@login_required()
def indexClient(request):
    all = client.objects.raw("select * from lcvoitures_client left join auth_user on lcvoitures_client.user_id =auth_user.id")
    return render(request, 'client/index.html', {'utilisateurs': all})

@login_required()
def indexReservation(request):
    reservations = reservation.objects.all().select_related('user' ,'voiture')
    return render(request,'reservation/index.html',{"reservations": reservations })

@login_required()
def chercherVoiture(request):
    resform = ReserveruneVoiture(request.POST or None)
    if request.method == 'POST':
        if resform.is_valid():
            datedeb = request.POST['dateDebut']
            datefin = request.POST['dateFin']
            voitures = voiture.objects.raw("SELECT * from lcvoitures_voiture WHERE immatriculation NOT in(SELECT lcvoitures_voiture.immatriculation FROM lcvoitures_voiture join lcvoitures_reservation on lcvoitures_reservation.voiture_id = lcvoitures_voiture.immatriculation WHERE DATE(lcvoitures_reservation.dateFin) BETWEEN '"+datedeb +"' and '" +datefin+"')")
            return render(request, 'reservation/voituresFiltred.html',{"voitures":voitures,"dateDebut" : datedeb , "dateFin":datefin, } )
    else:
        return render(request, 'reservation/reserver.html/' )






@csrf_exempt
@login_required()
def AjouterVoiture(request):

    msg = None
    succes=False
    m = marque.objects.all()
    tp = type_voiture.objects.all()
    ajoutForm = AjouterVoitureForm(request.POST or None)
    imagefom = AjouterVoitureForm(request.POST or None,request.FILES or None)

    if request.method == 'POST':
        photos = request.FILES.getlist('image')
        mod = request.POST['model']
        immatriculation = request.POST['immatriculation']
        couleur = request.POST['couleur']
        marqueId = request.POST['marque']
        typeID = request.POST['type_voiture']
        prixj = request.POST['prix_journalier']
        desc = request.POST['description']
        if ajoutForm.is_valid() and imagefom.is_valid():
            voiture.objects.create(immatriculation=immatriculation,couleur=couleur,marque_id=marqueId,type_voiture_id=typeID,model=mod,prix_journalier=prixj,description =desc,dispo=True)
            for ima in photos :
                photo_image.objects.create(image=ima, voiture_id=immatriculation )
            return redirect('/voitures')

    return render(request, 'voitures/Ajoutervoiture.html',{"marques":m,"types":tp,"ajout":ajoutForm,"message":msg,"succes":succes,"photos":imagefom})
@login_required()
def AjouterClient(request):
    adduserForm = SignUpForm(request.POST or None)
    clienForm = addClientfrom(request.POST or None)
    if request.method == 'POST':
        if adduserForm.is_valid() and clienForm.is_valid():
            adduserForm.save()
            nom = adduserForm.cleaned_data.get('last_name')
            prenom = adduserForm.cleaned_data.get('first_name')
            email = adduserForm.cleaned_data.get('email')
            pseudo = adduserForm.cleaned_data.get('username')
            password1 = adduserForm.cleaned_data.get('password1')
            tel = clienForm.cleaned_data.get('telephone')
            user = authenticate(username = pseudo,password=password1,email=email,last_name =nom, first_name = prenom,is_superuser=False,is_staff=False)
            cl = client(user=user,telephone=tel)
            cl.save()
            return redirect("/clients")


    return  render(request,'client/ajouterClient.html',{"user":adduserForm,"client":clienForm})

@login_required()
def DetailVoiture(request,immatriculation ):
    v = voiture.objects.get(immatriculation = immatriculation)
    im = photo_image.objects.raw("select  * FROM lcvoitures_photo_image WHERE voiture_id = 'BBBBBB'")

    return render(request,'voiturePage/index.html',{"voiture":v,"images":im})

@login_required()
def ajouterEmploye(request):
    userForm = SignUpForm(request.POST or None)
    employetForm = employeForm(request.POST or None)
    if request.method == 'POST':
        if userForm.is_valid() and employetForm.is_valid():
            nom = userForm.cleaned_data.get('last_name')
            prenom = userForm.cleaned_data.get('first_name')
            email = userForm.cleaned_data.get('email')
            pseudo = userForm.cleaned_data.get('username')
            password1 = userForm.cleaned_data.get('password1')
            salaire = employetForm.cleaned_data.get('salaire')
            user = User.objects.create_user(username=pseudo, password=password1, email=email, last_name=nom, first_name=prenom, is_superuser=False)
            user.is_staff = True
            user.save()
            cl = employe(user=user, salaire=salaire)
            cl.save()
    return render(request, 'employe/ajouterEmploye.html', {"user": userForm, "employe": employeForm})


@login_required()
def mdifierClient(request, id):
    cl = client.objects.get(id=id)
    user= User.objects.get(client = cl)

    userForm = MyUserChangeForm(request.POST or None , instance=user)
    clientForm = addClientfrom(request.POST or None , instance=cl)
    if request.method == 'POST':
        if userForm.is_valid() and clientForm.is_valid():
            userForm.save()
            clientForm.save()

            return redirect('/clients')

    return render(request,'client/modifierClient.html',{"client":clientForm,"user":userForm})
@login_required()
def modifierEmploye(request,id):
    emp = employe.objects.get(id =id)
    usr = User.objects.get(employee=emp)
    userForm = MyUserChangeForm(request.POST or None , instance=usr)
    employetForm = employeForm(request.POST or None, instance =emp )
    if request.method == 'POST':
        if userForm.is_valid() and employetForm.is_valid():
            userForm.save()
            employetForm.save()
            return redirect('/employés')
    return render(request, 'employe/modifierEmploye.html', {"user": userForm, "employe": employetForm})


@login_required()
def modifierVoiture(request, immatriculation):
    v = voiture.objects.get(immatriculation = immatriculation)
    types= type_voiture.objects.all()
    ma = marque.objects.all()
    voitureForm = AjouterVoitureForm(request.POST or None, instance=v)
    if request.method =="POST":
        if voitureForm.is_valid():
            voitureForm.save()
            return redirect('voitures')

    return render(request,'voitures/modifierVoiture.html',{"voiture":voitureForm,"marques":ma,"types":types})




@login_required()
def modifierCompte(request):
    changeForm = passwordChange(user=request.user , data=request.POST or None )
    if request.method == 'POST':
        if changeForm.is_valid():
            user =changeForm.save()
            update_session_auth_hash(request, user)
            messages.success(request,'mot de passe modifié')
    return render(request, 'user/modifierCompte.html',{"user":changeForm})

@login_required()
def supprimer_voiture(request,immatriculation):
    v = voiture.objects.get(immatriculation=immatriculation)
    v.delete()
    return redirect('voitures')



@login_required()
def supprimer_client(request,id):
    c = client.objects.get(id=id)
    user = User.objects.get(client=c)
    c.delete()
    user.delete()
    return redirect('/clients')

@login_required()
def supprimer_employe(request, id):
    c= employe.objects.get(id=id)
    user= User.objects.get(employee=c)
    c.delete()
    user.delete()
    return redirect('/employés')

@login_required()
def   ajouterReservation(request,immatriculation,dateDebut, dateFin ):
    res = reservation(user=request.user,voiture_id=immatriculation,dateDebut=dateDebut,dateFin=dateFin)
    res.save()

    return redirect('/mesReservations')