from django.shortcuts import render

def doctor_profile(request):
    context = {
        'name': 'Dr. Pruthvi Darji',
        'specialization': 'Cardiologist',
        'experience': '10 Years',
        'hospital': 'City Hospital',
        'email': 'pruthvidarji1123@gmail.com',
        'phone': '+919876543210',
    }
    return render(request, 'profileapp/doctor.html', context)

# Create your views here.
