from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # KELEN SİHİRLİ SATIR: Eğer kullanıcı sadece /account/ yazıp bırakırsa, direkt login'e şutla
    path('', lambda request: redirect('login')), 
    
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('change-password/', views.change_password, name='change_password'),




]
