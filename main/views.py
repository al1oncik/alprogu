from django.shortcuts import render


def index(request):
    return render(request, 'main/base.html')


def registration(request):
    return render(request, 'main/registration.html')
