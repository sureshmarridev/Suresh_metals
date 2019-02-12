from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You are seeing Suresh Metals")


def empty(request):
    return HttpResponse("This page is empty")

def login(request):
    return render(request, 'seed_corp/login.html')

def summary(request):
    return render(reqest, 'seed_corp/summary.html')