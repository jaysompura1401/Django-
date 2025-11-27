from django.shortcuts import render

def patient_form(request):
    return render(request, 'register/form.html')
