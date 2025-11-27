from django.db import models

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Pediatrician', 'Pediatrician'),
        ('Orthopedic', 'Orthopedic'),
        ('Neurologist', 'Neurologist'),
    ]

    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    availability = models.CharField(max_length=50, help_text="e.g., Mon–Fri, 10 AM–5 PM")
    experience_years = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"
