import re
import pyotp
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from users.models import Profile as useri

# Create your views here.
nombre=""

def generar_otp():
    base32secret3232 = pyotp.random_base32()
    totp = pyotp.TOTP('base32secret3232')
    otp=totp.now() # => '492039'
    return otp, totp

def verificar(totp, codigo):
    c=totp.verify(codigo, valid_window=1)
    return c

def login_view(request):

    if request.method == 'POST':
   
        otp, totp = generar_otp()
        
        username = request.POST.get('username')
        password = request.POST['password']
        codigo= request.POST.get('otp')
        if verificar(totp, codigo):
            return render(request, 'home/main.html')
        subject="Verifica tu cuenta"
        message= "Por favor verifica tu cuenta ingresando este código: " + otp
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['simongiraldoc@gmail.com']

        send_mail(subject, message, email_from, recipient_list)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'otp.html', {"email" : 'simongiraldoc@gmail.com'})
        else:
            return render(request, 'login/index.html', {'error': 'Nombre de usuario y/o contraseña invalidos'})

    return render(request, 'login/index.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
