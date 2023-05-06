# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from lcvoitures.models import voiture
from .forms import LoginForm, SignUpForm,addClientfrom
from lcvoitures.models import client


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)

        form2=addClientfrom(request.POST)

        if form.is_valid() and form2.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            first_name = form.cleaned_data.get("prenom")
            last_name = form.cleaned_data.get("nom")
            email = form.cleaned_data.get("email")
            telephone = form2.cleaned_data.get("telephone")
            user = authenticate(username=username, password=raw_password,last_name=last_name,first_name=first_name,email=email)
            c= client(user=user,telephone=telephone)
            c.save()

            msg = 'Vous avez créer votre - <a href="/login">Connexion</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})