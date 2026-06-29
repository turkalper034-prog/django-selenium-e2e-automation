from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

def login(request):
    from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == "POST":
        # Kullanıcı butona bastıysa, formdan gelen verileri yakala
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Kullanıcı adı ve şifre doğruysa kullanıcıyı veritabanından bul
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                auth_login(request, user) # Kullanıcıyı sisteme al (oturum aç)
                return redirect('Home') # Seni ana sayfaya fırlatır!
    else:
        # Kullanıcı sayfaya ilk defa girdiyse (GET), boş form göster
        form = AuthenticationForm()
        
    return render(request, "account/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Hazır formu gelen verilerle doldur
        if form.is_valid():
            user = form.save() # Kullanıcıyı veritabanına kaydet
            auth_login(request, user) # Otomatik giriş yaptır (Kullanıcı konforu)
            return redirect('Home')
    else:
        form = UserCreationForm() # Sayfa ilk açıldığında boş form göster
        
    return render(request, "account/register.html", {"form": form})


def logout(request):
    auth_logout(request)
    return redirect("/")



def change_password(request):
    if request.method == 'POST':
        # Giriş yapmış olan kullanıcının verileriyle formu doldur
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Şifre değiştiği için Django güvenlik amacıyla session'ı sıfırlamasın diye bunu çağırıyoruz
            update_session_auth_hash(request, user)
            return redirect('Home') # Başarılıysa ana sayfaya fırlat
    else:
        form = PasswordChangeForm(request.user)
        if 'old_password' in form.fields:
            form.fields['old_password'].label = "Mevcut Şifreniz"
            
        if 'new_password1' in form.fields:
            form.fields['new_password1'].label = "Yeni Şifre"
            form.fields['new_password1'].help_text = "Şifreniz en az 8 karakter olmalı ve çok yaygın olmamalıdır."
            
        if 'new_password2' in form.fields:
            form.fields['new_password2'].label = "Yeni Şifre (Tekrar)"
            form.fields['new_password2'].help_text = "Kontrol için yeni şifrenizi tekrar girin."
        
    return render(request, 'account/change_password.html', {'form': form})
