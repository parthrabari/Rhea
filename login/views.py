from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def Home(request):

def index(request):
    return render(request,"login/index.html")

def register(request):
    return render(request,"login/register.html")
