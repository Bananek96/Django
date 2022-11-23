from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .models import Person
from users.forms import UserLoginForm, UserForm, UserModelForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            p = Person(first_name=form.cleaned_data['first_name'],
                       last_name=form.cleaned_data['last_name'],
                       email=form.cleaned_data['email'],
                       job_title=form.cleaned_data['job_title'],
                       bio=form.cleaned_data['bio']
                       )
            p.save()
            messages.success(request, "Poprawnie dodano informacje!")
            return redirect(reverse('users:people'))
        else:
            messages.error(request, "Niepoprawne dane!")
    else:
        form = UserForm()

    people = Person.objects.all()
    kontekst = {'people': people, 'form': form}
    return render(request, 'users/index.html', kontekst)


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


@method_decorator(login_required, name='dispatch')
class ChangePeople(SuccessMessageMixin, UpdateView):
    model = Person
    form_class = UserModelForm
    template_name = 'users/index.html'
    success_message = 'Zaktualizowano informacje użytkownika!'

    def get_context_data(self, **kwargs):
        context = super(ChangePeople, self).get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        return context
