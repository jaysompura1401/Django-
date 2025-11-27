from django.shortcuts import render

def home(request):
    # simple view that renders templates/home.html
    return render(request, 'home.html')
