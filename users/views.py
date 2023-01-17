from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth
from django.http import HttpResponseRedirect
from users.forms import UserRegistrationForm, UserLoginForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request.user)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}

    return render(request, 'users/register.html', context)
