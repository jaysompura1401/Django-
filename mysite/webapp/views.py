from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Django!</h1><p>This is your first webpage.</p>")
# Create your views here.
