
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Student, Course, Assignment, Exam, Note

# utility:

def get_courses():
    courses = Course.objects.all()
    courses = sorted(courses, key=lambda x: x.due_date)
    return courses


def get_assignments():
    assignments = Assignment.objects.all()
    assignments = sorted(assignments, key=lambda x: x.due_date)
    return assignments


def get_exams():
    exams = Exam.objects.all()
    exams = sorted(exams, key=lambda x: x.date)
    return exams


def get_notes():
    notes = Note.objects.all()
    notes = sorted(notes, key=lambda x: x.creation_date)
    return notes

# views:

def index(request):
    return render(request, 'studi/index.html')   


def login(request):
    return render(request, 'studi/login.html')   


def register(request):
    return render(request, 'studi/register.html')   


def profile(request):
    student = Student.objects.first()
    context = {
        'student': student
    }
    return render(request, 'studi/profile.html', context)


def dashboard(request):
    student = Student.objects.first()
    courses = get_courses()
    assignments = get_assignments()
    exams = get_exams()
    notes = get_notes()
    context = {
        'first_name': student.first_name,
        'last_name': student.last_name,
        'schedule': student.schedule,
        'current_week': student.current_week,
        'exams': exams,
        'notes': notes,
        'assignments': assignments
    }
    return render(request, 'studi/dashboard.html', context)    


def courses(request):
    courses = get_courses()
    context = {
        'courses': courses
    }
    return render(request, 'studi/courses.html', context)
    

def assignments(request):
    assignments = get_assignments()
    context = {
        'assignments': assignments
    }
    return render(request, 'studi/assignments.html', context)


def exams(request):
    exams = get_exams()
    context = {
        'exams': exams
    }
    return render(request, 'studi/exams.html', exams)


def notes(request):
    notes = get_notes()
    context = {
        'notes': notes
    }
    return render(request, 'studi/notes.html', context)


@require_POST
def add_course(request):
    course = Course(
        code = request.POST.get('code'),
        name = request.POST.get('name'),
        department = Department.objects.filter(id=request.POST.get('department_id')).first(),
    )
    course.save()
    return redirect('studi:courses')


@require_POST
def delete_course(request):
    course = Course.objects.filter(id=request.POST.get('id')).first()
    course.delete()
    return redirect('studi:courses')


@require_POST
def add_assignment(request):
    assignment = Assignment(
        name = request.POST.get('name'),
        due_date = request.POST.get('due_date'),
    )
    assignment.save()
    return redirect('studi:assignments')


@require_POST
def delete_assignment(request):
    assignment = Assignment.objects.filter(id=request.POST.get('id')).first()
    assignment.delete()
    return redirect('studi:assignments')


@require_POST
def add_exam(request):
    exam = Exam(
        name = request.POST.get('name'),
        course = Course.objects.filter(id=request.POST.get('course_id')).first(),
        date = request.POST.get('date'),
    )
    exam.save()
    return redirect('studi:exams')


@require_POST
def delete_exam(request):
    exam = Exam.objects.filter(id=request.POST.get('id')).first()
    exam.delete()
    return redirect('studi:exams')


@require_POST
def add_note(request):
    note = Note(
        title = request.POST.get('name'),
        content = request.POST.get('content'),
    )
    note.save()
    return redirect('studi:notes')


@require_POST
def delete_note(request):
    note = Note.objects.filter(id=request.POST.get('id')).first()
    note.delete()
    return redirect('studi:notes')


@require_POST
def set_schedule(request):
    student = Student.objects.first()
    student.schedule = request.POST.get('schedule')
    return redirect('studi:dashboard')


@require_POST
def set_profile(request):
    student = Student.objects.first()
    student.first_name = request.POST.get('first_name')
    student.last_name = request.POST.get('last_name')
    student.email_address = request.POST.get('email_address')
    return redirect('studi:profile')

# maintenance:

def create_student(request):
    student = Student(
        current_week=4,
        email_address = 'a@a.a',
        first_name = 'Jane',
        last_name = 'Doe',
        schedule = '{}',
    )
    student.save()
    return HttpResponse('Done.')
