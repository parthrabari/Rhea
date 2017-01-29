from django.shortcuts import render,redirect,HttpResponseRedirect,render_to_response
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib import messages
from django.template import RequestContext
from .models import LoginData

# Create your views here.
# def Home(request):

def index(request):
    return render(request,"login/index.html")

def success(request):
    return render(request,"login/success.html")


def register(request):
    if request.method == 'POST':
        form = LoginForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.add_message(request, messages.INFO, 'Your Registrtion completed succesffully, Your id is-' + str(instance.pk))
            return HttpResponseRedirect('success')
    else:
        form = LoginForm()
    context = {
        "form":form,
    }
    return render(request,"login/register.html",context)


def all_data(request):
     queryset = LoginData.objects.all()
     context = {
        "o_list" : queryset,
        "title": "List"
     }
     return render(request,"login/viewReg.html",context)
