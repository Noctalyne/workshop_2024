from django.shortcuts import render

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