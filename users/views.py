import re
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def login_view(request):

    if request.method == 'POST':
   
        username = request.POST['username']
        password = request.POST['password']

        subject="Verifica tu cuenta"
        message= "Por favor verifica tu cuenta leyendo este código QR: "
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
    