from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Doctor

def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctorapp/home.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        doctor = Doctor.objects.create(name=name, specialization=specialization, phone=phone, email=email)
        return JsonResponse({'id': doctor.id, 'name': doctor.name, 'specialization': doctor.specialization, 'phone': doctor.phone, 'email': doctor.email})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def update_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        doctor.name = request.POST.get('name')
        doctor.specialization = request.POST.get('specialization')
        doctor.phone = request.POST.get('phone')
        doctor.email = request.POST.get('email')
        doctor.save()
        return JsonResponse({'id': doctor.id, 'name': doctor.name, 'specialization': doctor.specialization, 'phone': doctor.phone, 'email': doctor.email})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    return JsonResponse({'deleted': True})
