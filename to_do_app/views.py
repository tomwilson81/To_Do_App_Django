from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    return render(request, 'index.html')