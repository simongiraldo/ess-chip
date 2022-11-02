from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile as useri 

# Create your views here.


def index(request):
    return render(request, 'saldo.html', {'estudiante': f'{useri.user}'})

