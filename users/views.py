import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):

    if request.method == 'POST':
   
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login/index.html', {'error': 'Nombre de usuario y/o contraseña invalidos'})

    return render(request, 'login/index.html')
    