from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def Home(request):


def index(request):
    return HttpResponse('A rom rom bhai')
