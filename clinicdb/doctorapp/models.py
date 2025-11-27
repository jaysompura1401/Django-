from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    experience = models.IntegerField()

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"
