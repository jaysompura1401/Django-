from django.shortcuts import render
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()  # get all doctors from database
    return render(request, 'advertise/doctor_list.html', {'doctors': doctors})
