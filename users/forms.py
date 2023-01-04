from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


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


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Imię",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    last_name = forms.CharField(
        label="Nazwisko",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.CharField(
        label="email",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email"
        ]


class EditUserProfileForm(forms.ModelForm):
    city = forms.CharField(
        label="Miasto",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    bio = forms.CharField(
        label="Bio",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = UserProfile
        fields = [
            "city",
            "bio"
        ]
