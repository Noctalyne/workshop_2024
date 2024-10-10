from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),

    path('connect/', views.connect, name='connect'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home' ),
    path('home/tuto/1/', views.tutoStepOne, name='tutoStepOne'),
    path('home/tuto/2/', views.tutoStepTwo, name='tutoStepTwo'),
    path('home/tuto/3/', views.tutoStepThree, name='tutoStepThree'),
    path('home/account/vitalSigns', views.vitalSigns, name='vitalSigns' ),
    path('home/account/medical/', views.medicalHistory, name='medicalHistory'),

    path('home/account/laboratoryResult/', views.laboratoryResult, name='laboratoryResult'),
    path('home/account/advice/', views.advice, name='advice'),
    path('home/account/findWatch/', views.findWatch, name='findWatch'),
    path('home/settings/', views.settings, name='settings'),
    path('home/settings/notifications/', views.notifications, name='notifications'),
    path('home/settings/apparence/', views.apparence, name='apparence'),

]