from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_form, name='patient_form'),
    
]
