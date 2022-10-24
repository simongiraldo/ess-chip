from email.policy import HTTP
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'main.html')
