from django.db import models

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
]


class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    contact_no = models.CharField(max_length=20)