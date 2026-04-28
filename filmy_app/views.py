from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

def home(request):
    film = Film.objects.all()
    return render(request, "filmy.html", {'filmy': film})