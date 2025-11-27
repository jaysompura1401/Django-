from django.shortcuts import render

def home(request):
    return render(request, 'mainapp/home.html')

def profile(request):
    return render(request, 'mainapp/profile.html')

def contact(request):
    return render(request, 'mainapp/contact.html')
