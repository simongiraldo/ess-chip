from email.policy import HTTP
from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'home/main.html')
