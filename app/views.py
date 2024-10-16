import json

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserForm, LoginForm, RegisterForm
from .models import User
from django.contrib.auth.models import User as AuthUser
import datetime

# Create your views here.

# 
def landing(request):
    return render(request, 'landing.html')

def authentification(request):
    # user = User.objects.create_user("user", "user@user.fr", "userPassword1234")
    # user.last_name = "user"
    # user.save()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Utilisation de l'authentification via le modèle utilisateur
            user = AuthUser.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                # Authentification réussie, connexion de l'utilisateur
                login(request, user)
                return redirect('home')  # Redirection après connexion réussie
            else:
                # Authentification échouée, affichage d'un message d'erreur
                messages.error(request, 'Email ou mot de passe incorrect.')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Ici, tu peux créer un utilisateur ou effectuer d'autres actions
            user = AuthUser.objects.create_user(full_name, email, password)
            if user is not None:
                # Authentification réussie, connexion de l'utilisateur
                login(request, user)
                messages.success(request, 'Inscription réussie.')
                return redirect('tutoStepOne')  # Redirection après inscription réussie
    else:
        form = RegisterForm()

    return render(request, 'user/register.html', {'form': form})

#  
def tutoStepOne(request):
    return render(request, 'tuto/stepOne.html')

def tutoStepTwo(request):
    return render(request, 'tuto/stepTwo.html')

def tutoStepThree(request):
    return render(request, 'tuto/stepThree.html')

# 
def home(request):
    return render(request, 'home/home.html')

def vitalSigns(request) :
    return render(request, 'home/vitalSigns.html')

def medicalHistory(request) :
    return render(request, 'home/medicalHistory.html')

def laboratoryResult(request) :
    return render(request, 'home/laboratoryResult.html')

def advice(request) :
    return render(request, 'home/advice.html')

def findWatch(request) :
    return render(request, 'home/findWatch.html')

# Vue à des fin de test
def underWork(request) :
    return render(request, 'components/workInProgress.html')


def settings(request) :
    return render(request, 'settings.html')

def notifications(request) :
    return render(request, 'settingsFolder/notifications.html')

def apparence(request) :
    return render(request, 'settingsFolder/apparence.html')


# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# def add_user(request):
#     if request.method == 'GET':
#         form = UserForm()
#         return render(request, 'add_user.html', {'form': form})
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         print("form is valid : ", form.is_valid())
#         if form.is_valid():
#             user = form.save(commit=False)
#             # site.user = request.user
#             user.save()
#             messages.success(request, 'L\' utilisateur ' + user.first_name + ' a bien été ajouté.')
#             return redirect('home')
#         else:
#             print(form.errors)
#             return redirect('add_user')
#     else:
#         messages.error(request, 'Une erreur est survenue.')
#         return redirect('home')