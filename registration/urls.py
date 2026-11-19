from django.urls import path
from . import views

urlpatterns = [
    # Module 06 - Existing Routes
    path('', views.student_registration, name='student_registration'),
    path('success/', views.registration_success, name='registration_success'),

    # Module 07 - New Routes
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # Module 08 - Staff Dashboard
    path('dashboard/', views.staff_dashboard, name='staff_dashboard'),
]