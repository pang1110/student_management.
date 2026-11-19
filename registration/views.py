from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Student
from .forms import StudentForm


# MODULE 06 - Existing Registration
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
        return redirect('registration_success')

    return render(request, 'registration/registration.html')


def registration_success(request):
    return render(request, 'registration/success.html')


# MODULE 07 - Student Directory
def student_list(request):
    query = request.GET.get('q', '').strip()

    students = Student.objects.all().order_by(
        'last_name', 'first_name'
    )

    if query:
        students = students.filter(
            Q(student_id__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    context = {
        'students': students,
        'query': query,
    }

    return render(
        request,
        'registration/student_list.html',
        context
    )


# Student Details
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    return render(
        request,
        'registration/student_detail.html',
        {'student': student}
    )


# Add Student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Student record created successfully.'
            )
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(
        request,
        'registration/student_form.html',
        {
            'form': form,
            'page_title': 'Register Student'
        }
    )


# Edit Student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Student record updated successfully.'
            )
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'registration/student_form.html',
        {
            'form': form,
            'page_title': 'Update Student',
            'student': student,
        }
    )


# Delete Student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        messages.success(
            request,
            'Student record deleted successfully.'
        )
        return redirect('student_list')

    return render(
        request,
        'registration/student_confirm_delete.html',
        {'student': student}
    )


# MODULE 08 - Staff Access Protection
def staff_check(user):
    return user.is_authenticated and user.is_staff


# MODULE 09 - Dashboard Enhancement and Basic Reporting
@user_passes_test(staff_check, login_url='login')
def staff_dashboard(request):

    # Student Summary
    total_students = Student.objects.count()

    male_students = Student.objects.filter(
        gender='Male'
    ).count()

    female_students = Student.objects.filter(
        gender='Female'
    ).count()

    # Gender Percentages
    male_percent = (
        male_students / total_students * 100
        if total_students > 0 else 0
    )

    female_percent = (
        female_students / total_students * 100
        if total_students > 0 else 0
    )

    # Read Search Term
    query = request.GET.get('q', '').strip()

    # Prepare Student Report
    students = Student.objects.all().order_by(
        Lower('last_name'),
        Lower('first_name')
    )

    # Search Multiple Fields
    if query:
        students = students.filter(
            Q(student_id__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    # Context Dictionary
    context = {
        'total_students': total_students,
        'male_students': male_students,
        'female_students': female_students,
        'male_percent': male_percent,
        'female_percent': female_percent,
        'students': students,
        'query': query,
    }

    return render(
        request,
        'registration/dashboard.html',
        context
    )