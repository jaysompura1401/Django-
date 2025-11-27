from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor

# CREATE and READ
def doctor_list(request):
    if request.method == "POST":
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        experience = request.POST.get('experience')
        Doctor.objects.create(
            name=name,
            specialization=specialization,
            email=email,
            phone=phone,
            experience=experience
        )
        return redirect('doctor_list')
    
    doctors = Doctor.objects.all()
    return render(request, 'doctorapp/doctor_list.html', {'doctors': doctors})


# UPDATE
def update_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        doctor.name = request.POST.get('name')
        doctor.specialization = request.POST.get('specialization')
        doctor.email = request.POST.get('email')
        doctor.phone = request.POST.get('phone')
        doctor.experience = request.POST.get('experience')
        doctor.save()
        return redirect('doctor_list')
    return render(request, 'doctorapp/update_doctor.html', {'doctor': doctor})


# DELETE
def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    return redirect('doctor_list')
