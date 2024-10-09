from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('add_user/', views.add_user, name='add_user'),
]