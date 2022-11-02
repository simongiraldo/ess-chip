import re
import pyotp
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def generar_otp():
    base32secret3232 = pyotp.random_base32()
    totp = pyotp.TOTP('base32secret3232')
    otp=totp.now() # => '492039'
    return otp

def login_view(request):

    if request.method == 'POST':
   
        otp = generar_otp()
        
        username = request.POST['username']
        password = request.POST['password']

        subject="Verifica tu cuenta"
        message= "Por favor verifica tu cuenta ingresando este código: " + otp
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [username]
        

        send_mail(subject, message, email_from, recipient_list)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login/index.html', {'error': 'Nombre de usuario y/o contraseña invalidos'})

    return render(request, 'login/index.html')
    
