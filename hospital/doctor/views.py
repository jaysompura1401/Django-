from django.shortcuts import render

def doctor_profile(request):
    context = {
        'name': 'Dr. Pruthvi Darji',
        'specialization': 'Cardiologist',
        'experience': '10 Years',
    }
    return render(request, 'doctor/profile.html', context)