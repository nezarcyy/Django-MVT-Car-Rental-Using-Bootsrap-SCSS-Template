from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.db.models import TextField
from django.forms import ModelForm, ImageField, CharField, IntegerField, FloatField
from phonenumber_field.formfields import PhoneNumberField

from lcvoitures.models import voiture, photo_image, type_voiture, reservation, client,employe
from django import forms


class AjouterVoitureForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(AjouterVoitureForm, self).__init__(*args, **kwargs)
            self.fields['type_voiture'].widget.attrs={"class":"form-control"}
            self.fields['marque'].widget.attrs ={"class":'form-control'}

        immatriculation = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"immatriculation"
                }
            )
        )
        model = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "model"
                }
            )
        )
        couleur = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Couleur"
                }
            )
        )
        description = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    "class":"form-control",
                    "placeholder":"description",
                    "row" : 3
                }
            )
        )
        prix_journalier=FloatField(
            widget=forms.NumberInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"prix journalier"
                }
            )
        )

        class Meta:
            model = voiture
            fields= ('immatriculation','model','couleur','marque','type_voiture','description','prix_journalier')




class Ajouterphoto_voitureForm(forms.ModelForm):
    image = ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "multiple": True,
                   }
        )
    )
    class Meta:
        model= photo_image
        fields= 'image',

class AjouterTypevoiture(forms.ModelForm):

    class Meta:
        model= type_voiture
        fields=('type',)


class ReserveruneVoiture(forms.Form):
    class Meta:
        model =reservation
        fields = '__all__'






class addClientfrom(forms.ModelForm):
    telephone = PhoneNumberField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "telephone",
                "class": "form-control"
            }
        ))
    class Meta:
        model = client
        fields=('telephone',)

class SignUpForm(UserCreationForm):


    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "pseudo",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"nom",
                "class": "form-control"
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
        fields = ('last_name', 'first_name', 'username', 'email', 'password1','password2')


class employeForm(forms.ModelForm):
    salaire=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "salaire",
                "class": "form-control",
            }
        )
    )
    class Meta:
        model = employe
        fields=('salaire',)




class MyUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Nom'}
        self.fields['first_name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Prenom'}
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'Email'}


    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email')

class passwordChange(PasswordChangeForm):
        def __init__(self, *args, **kwargs):
            super(passwordChange, self).__init__(*args, **kwargs)
            self.fields['old_password'].label = "Ancien mot de passe"
            self.fields['new_password1'].label = "Nouveau mot de passe"
            self.fields['new_password2'].label = "Confirmation de mot de passe"




        old_password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "placeholder": "ancien mot de passe",
                    "class": "form-control",
                }
            )
        )
        new_password1 = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "placeholder": "nouveau mot de passe",
                    "class": "form-control",
                }
            )
        )

        new_password2 = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "placeholder": "confirmation de nouveau mot de passe",
                    "class": "form-control",
                }
            )
        )

        class Meta:
                model=User
                fields =('old_password','new_password1','new_password2')



