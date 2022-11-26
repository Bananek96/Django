from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .models import User
from users.forms import UserLoginForm, UserForm

from django.views.generic import ListView


def index(request):
    return render(request, 'users/index.html')


def rejestruj(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Utworzono konto! Możesz się zalogować!")
            return redirect(reverse('users:index'))
    else:
        form = UserCreationForm()

    kontekst = {'form': form}
    return render(request, 'users/rejestruj.html', kontekst)


def loguj_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            nazwa = form.cleaned_data['login']
            haslo = form.cleaned_data['haslo']
            user = authenticate(request, username=nazwa, password=haslo)
            if user is not None:
                login(request, user)
                messages.success(request, "Zostałeś zalogowany!")
                return redirect(reverse('users:index'))
            else:
                messages.error(request, "Błędny login lub hasło!")
    else:
        form = UserLoginForm()

    kontekst = {'form': form}
    return render(request, 'users/loguj_user.html', kontekst)


def wyloguj_user(request):
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('users:index'))


def users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            p = User(first_name=form.cleaned_data['first_name'],
                     last_name=form.cleaned_data['last_name'],
                     email=form.cleaned_data['email'],
                     job_title=form.cleaned_data['job_title'],
                     bio=form.cleaned_data['bio']
                     )
            p.save()
            messages.success(request, "Poprawnie dodano informacje!")
            return redirect(reverse('users:users'))
        else:
            messages.error(request, "Niepoprawne dane!")
    else:
        form = UserForm()

    user = User.objects.all()
    kontekst = {'users': user, 'form': form}
    return render(request, 'users/user_info.html', kontekst)


class UsersList(ListView):
    model = User
    context_object_name = 'Informacje'
    template_name = 'users/user_info.html'
