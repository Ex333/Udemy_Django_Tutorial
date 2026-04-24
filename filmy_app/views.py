from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("To jest nasz pierwszy TEST!")
    return render(request, "base.html")