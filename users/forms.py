from django import forms
from django.forms import ModelForm
from users.models import *


class UserLoginForm(forms.Form):
    login = forms.CharField(
        label="Twój login",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    haslo = forms.CharField(
        label="Twoje hasło",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'})
    )


class UserForm(forms.Form):
    first_name = forms.CharField(
        label="Imie",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label="Nazwisko",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    city= forms.CharField(
        label="Miasto",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    bio = forms.CharField(
        label="BIO",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class UserModelForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'city', 'bio',)
