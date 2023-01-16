from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from users.forms import UserRegistrationForm


def login(request):
    ...


def logout(request):
    ...


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
