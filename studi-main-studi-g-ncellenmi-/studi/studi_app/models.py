
# For the purpose of prototyping, a single Student row exists, each row in other tables belonging to that student.

from django.db import models
from django.utils.timezone import now


class Student(models.Model):
    email_address = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    current_week = models.IntegerField()
    schedule = models.TextField()


class Department(models.Model):
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=4)


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=64)


class Assignment(models.Model):
    course = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    due_date = models.DateField()


class Exam(models.Model):
    course = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    date = models.DateField()


class Note(models.Model):
    creation_date = models.DateTimeField(default=now, editable=False) 
    title = models.CharField(max_length=128)
    content = models.TextField()
