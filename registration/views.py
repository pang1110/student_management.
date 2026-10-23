from django.shortcuts import render, redirect
from .models import Student

def student_registration(request):
    if request.method == 'POST':
        Student.objects.create(
            student_id=request.POST['student_id'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            gender=request.POST['gender'],
            date_of_birth=request.POST['date_of_birth'],
            contact_no=request.POST['contact_no']
        )
        return render(request, 'registration/success.html')

    return render(request, 'registration/registration.html')