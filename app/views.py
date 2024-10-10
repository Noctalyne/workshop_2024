import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserForm
import datetime

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')

def connect(request):
    return render(request, 'connect.html')

def register(request):
    return render(request, 'register.html')

def tutoStepOne(request):
    return render(request, 'tuto/stepOne.html')

def tutoStepTwo(request):
    return render(request, 'tuto/stepTwo.html')

def tutoStepThree(request):
    return render(request, 'tuto/stepThree.html')

def vitalSigns(request) :
    return render(request, 'account/vitalSigns.html')

def medicalHistory(request) :
    return render(request, 'account/medicalHistory.html')

def laboratoryResult(request) :
    return render(request, 'account/laboratoryResult.html')

def advice(request) :
    return render(request, 'account/advice.html')

def findWatch(request) :
    return render(request, 'account/findWatch.html')

# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def add_user(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'add_user.html', {'form': form})
    if request.method == 'POST':
        form = UserForm(request.POST)
        print("form is valid : ", form.is_valid())
        if form.is_valid():
            user = form.save(commit=False)
            # site.user = request.user
            user.save()
            messages.success(request, 'L\' utilisateur ' + user.first_name + ' a bien été ajouté.')
            return redirect('home')
        else:
            print(form.errors)
            return redirect('add_user')
    else:
        messages.error(request, 'Une erreur est survenue.')
        return redirect('home')