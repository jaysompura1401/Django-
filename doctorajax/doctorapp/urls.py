from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_doctor, name='add_doctor'),
    path('update/<int:id>/', views.update_doctor, name='update_doctor'),
    path('delete/<int:id>/', views.delete_doctor, name='delete_doctor'),
]
