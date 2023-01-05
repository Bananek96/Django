from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from users.forms import UserLoginForm, EditUserForm, EditUserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
                return redirect(reverse('forum:index'))
            else:
                messages.error(request, "Błędny login lub hasło!")
    else:
        form = UserLoginForm()

    kontekst = {'form': form}
    return render(request, 'users/loguj_user.html', kontekst)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('forum:index')
    template_name = 'users/loguj_user.html'


def wyloguj_user(request):
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('forum:index'))


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    userprofile = user.userprofile
    return render(request, 'users/index.html', {'userprofile': userprofile})


def edit_user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_profile = user.userprofile

    user_form = EditUserForm(request.POST or None, instance=user)
    profile_form = EditUserProfileForm(request.POST or None, instance=user_profile)

    if request.method == "POST" and user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect(f"/users/{pk}")

    return render(request, "users/user_info.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })
