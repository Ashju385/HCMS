import datetime
from multiprocessing import context
from django.shortcuts import render,redirect
from base.models import Member,Service
from .forms import ServiceForm
from django.contrib.auth.forms import UserCreationForm
from datetime import date
# Create your views here.
def signup(request):
    form = UserCreationForm()
    if request.method =='POST':
       form = UserCreationForm(request.POST) 
       if form.is_valid():
        form.save()
    context ={'form':form}
    return render(request,'base/signup_form.html',context)

def login(request):
    return render(request,'base/login_form.html')

def home(request):
    return render(request,'base/home.html')


def member(request):
    members= Member.objects.all()

    return render(request,'base/member.html',{'members': members})

def services(request):
    form = ServiceForm()
    if request.method == 'POST':
        form= ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('response/')

    context={'form':form}
    return render(request,'base/services.html',context)

def reply(request):
    return render(request,'base/response.html')