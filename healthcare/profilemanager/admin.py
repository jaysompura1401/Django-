from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience', 'hospital_name', 'available')
    list_filter = ('specialization', 'available')
    search_fields = ('name', 'specialization', 'hospital_name')
    ordering = ('name',)
    list_editable = ('available',)

