from django.shortcuts import render
import json


from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You are seeing Suresh Metals")


def empty(request):
    return HttpResponse("This page is empty")

def login(request):
    return render(request, 'seed_corp/login.html')
