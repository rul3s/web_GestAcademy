from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.

def login_view(request):
    template = loader.get_template('AcademyApp/login.html')
    return HttpResponse(template.render())


def logout_view(request):
    logout(request)
    return render(request, 'AcademyApp/logout.html', {})


def auth_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return redirect("index")

        else:
            # Return a 'disabled account' error message
            template = loader.get_template('AcademyApp/error.html')
    else:
        # Return an 'invalid login' error message.
        template = loader.get_template('AcademyApp/error.html')

    return HttpResponse(template.render())

@login_required
def index(request):
    return render(request, 'AcademyApp/index.html', {})

@login_required
def add_std(request):
    if request.method == 'POST':
        form = StdForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('get/list')
    else:
        form = StdForm()

    return render(request, 'AcademyApp/addStudent.html', {'form': form})

@login_required
def edit_std(request, student_id=None):
    obj = get_object_or_404(Student, pk=student_id)
    form = StdForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return students(request)
    return render(request, 'AcademyApp/addStudent.html', {'form': form})

@login_required
def rem_std(request, student_id):
    Student.objects.get(pk=student_id).delete()
    return students(request)

@login_required
def students(request):
    students_list = Student.objects.order_by('registered')
    template = loader.get_template('AcademyApp/students.html')
    context = RequestContext(request, {
        'students_list': students_list,
    })

    return HttpResponse(template.render(context))

@login_required
def student(request, student_id):
    try:
        std = Student.objects.get(pk=student_id)
        context = {'std': std}
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'AcademyApp/student.html', context)
    # return HttpResponse("You're looking for student %s" % student_id)
    # return HttpResponse("Name = " +std.name)

@login_required
def studentsjson(request):
    return HttpResponse(serializers.serialize('json', Student.objects.all()))

@login_required
def studentsxml(request):
    return HttpResponse(serializers.serialize('xml', Student.objects.all()))

@login_required
def add_tchr(request):
    if request.method == 'POST':
        form = TchrForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('get/list')
    else:
        form = TchrForm()

    return render(request, 'AcademyApp/addTeacher.html', {'form': form})

@login_required
def edit_tchr(request, teacher_id):
    obj = get_object_or_404(Teacher, pk=teacher_id)
    form = TchrForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return teachers(request)
    return render(request, 'AcademyApp/addTeacher.html', {'form': form})

@login_required
def rem_tchr(request, teacher_id):
    Teacher.objects.get(pk=teacher_id).delete()
    return teachers(request)

@login_required
def teachers(request):
    teachers_list = Teacher.objects.order_by('registered')
    context = {'teachers_list': teachers_list}

    return render(request, 'AcademyApp/teachers.html', context)

@login_required
def teacher(request, teacher_id):
    try:
        tchr = Teacher.objects.get(pk=teacher_id)
        context = {'tchr': tchr}
    except Teacher.DoesNotExist:
        raise Http404("Teacher does not exist")
    return render(request, 'AcademyApp/teacher.html', context)

@login_required
def teachersjson(request):
    return HttpResponse(serializers.serialize('json', Teacher.objects.all()))

@login_required
def teacherssxml(request):
    return HttpResponse(serializers.serialize('xml', Teacher.objects.all()))

@login_required
def add_acdmy(request):
    if request.method == 'POST':
        form = AcdmyForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('get/list')
    else:
        form = AcdmyForm()

    return render(request, 'AcademyApp/addAcademy.html', {'form': form})

@login_required
def edit_acdmy(request, academy_id):
    obj = get_object_or_404(Academy, pk=academy_id)
    form = AcdmyForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return academies(request)
    return render(request, 'AcademyApp/addAcademy.html', {'form': form})

@login_required
def rem_acdmy(request, academy_id):
    Academy.objects.get(pk=academy_id).delete()
    return academies(request)

@login_required
def academies(request):
    academies_list = Academy.objects.order_by('registered')
    context = {'academies_list': academies_list}

    return render(request, 'AcademyApp/academies.html', context)

@login_required
def academy(request, academy_id):
    try:
        acdmy = Academy.objects.get(pk=academy_id)
        context = {'acdmy': acdmy}
    except Academy.DoesNotExist:
        raise Http404("Academy does not exist")
    return render(request, 'AcademyApp/academy.html', context)

@login_required
def academiesjson(request):
    return HttpResponse(serializers.serialize('json', Academy.objects.all()))

@login_required
def academiesxml(request):
    return HttpResponse(serializers.serialize('xml', Academy.objects.all()))