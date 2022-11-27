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


class UserModelForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'city', 'bio',)
