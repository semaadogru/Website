
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),

    path("profile/", views.profile, name="profile"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("courses/", views.courses, name="courses"),
    path("assignments/", views.assignments, name="assignments"),
    path("exams/", views.exams, name="exams"),
    path("notes/", views.notes, name="notes"),

    path("add_course/", views.add_course, name="add_course"),
    path("delete_course/", views.delete_course, name="delete_course"),
    path("add_assignment/", views.add_assignment, name="add_assignment"),
    path("delete_assignment/", views.delete_assignment, name="delete_assignment"),
    path("add_exam/", views.add_exam, name="add_exam"),
    path("delete_exam/", views.delete_exam, name="delete_exam"),
    path("add_note/", views.add_note, name="add_note"),
    path("delete_note/", views.delete_note, name="delete_note"),

    path("set_schedule/", views.set_schedule, name="set_schedule"),
    path("set_profile/", views.set_profile, name="set_profile"),
    

    path("maintenance/create_student/", views.create_student, name="create_student"),
]
