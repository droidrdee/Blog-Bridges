from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'blog/home.html')


def login(request):
    return render(request, 'blog/login.html')


def signup(request):
    return render(request, 'blog/signup.html')


