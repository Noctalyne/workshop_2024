import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserForm
import datetime

# Create your views here.
def landing(request):
    print(datetime.date)
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')

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