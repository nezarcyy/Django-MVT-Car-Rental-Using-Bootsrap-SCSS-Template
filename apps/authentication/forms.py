
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from lcvoitures.models import client


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "nom d'utilisateur",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "mot de passe",
                "class": "form-control"
            }
        )
    )



class addClientfrom(forms.Form):
    telephone = PhoneNumberField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "pseudo",
                "class": "form-control"
            }
        ))
    class Meta:
        User = client;
        fields=('telephone')

class SignUpForm(UserCreationForm):


    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "peseudo",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"nom",
                "class":"form-control"
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "prenom",
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    telephone= PhoneNumberField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"Télephone",
                "class" : "form-control",
            }
        )

    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "mot de passe",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "verfifcation mot de passe",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('last_name','first_name','username','email', 'password1', 'password2')
