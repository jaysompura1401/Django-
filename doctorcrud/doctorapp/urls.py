from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('update/<int:id>/', views.update_doctor, name='update_doctor'),
    path('delete/<int:id>/', views.delete_doctor, name='delete_doctor'),
]
