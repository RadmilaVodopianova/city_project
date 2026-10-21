
from django.shortcuts import render


def home(request):
    return render(request, 'sport/home.html')


def football(request):
    return render(request, 'sport/football.html')


def hockey(request):
    return render(request, 'sport/hockey.html')


def basketball(request):
    return render(request, 'sport/basketball.html')

