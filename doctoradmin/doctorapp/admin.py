from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    # Fields shown in list view
    list_display = ('name', 'specialization', 'availability', 'experience_years', 'active')

    # Fields that can be filtered
    list_filter = ('specialization', 'active', 'experience_years')

    # Fields that can be searched
    search_fields = ('name', 'specialization', 'email', 'phone')

    # Read-only fields
    readonly_fields = ('email',)

    # Group fields in form
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'specialization', 'experience_years')
        }),
        ('Contact Details', {
            'fields': ('phone', 'email')
        }),
        ('Availability & Status', {
            'fields': ('availability', 'active')
        }),
    )

    # Add ordering
    ordering = ('name',)

    # Change list display per page
    list_per_page = 10
