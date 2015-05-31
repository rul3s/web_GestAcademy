from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, Http404
from models import *
from django.template import RequestContext, loader
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect


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


def index(request):
    return render(request, 'AcademyApp/index.html', {})


def students(request):
    students_list = Student.objects.order_by('registered')
    template = loader.get_template('AcademyApp/students.html')
    context = RequestContext(request, {
        'students_list': students_list,
    })

    return HttpResponse(template.render(context))


def student(request, student_id):
    try:
        std = Student.objects.get(pk=student_id)
        context = {'std': std}
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'AcademyApp/student.html', context)
    # return HttpResponse("You're looking for student %s" % student_id)
    # return HttpResponse("Name = " +std.name)


def studentsjson(request):
    return HttpResponse(serializers.serialize('json', Student.objects.all()))


def studentsxml(request):
    return HttpResponse(serializers.serialize('xml', Student.objects.all()))


def teachers(request):
    teachers_list = Teacher.objects.order_by('registered')
    context = {'teachers_list': teachers_list}

    return render(request, 'AcademyApp/teachers.html', context)


def teacher(request, teacher_id):
    try:
        tchr = Teacher.objects.get(pk=teacher_id)
        context = {'tchr': tchr}
    except Teacher.DoesNotExist:
        raise Http404("Teacher does not exist")
    return render(request, 'AcademyApp/teacher.html', context)


def teachersjson(request):
    return HttpResponse(serializers.serialize('json', Teacher.objects.all()))


def teacherssxml(request):
    return HttpResponse(serializers.serialize('xml', Teacher.objects.all()))


def academies(request):
    academies_list = Academy.objects.order_by('registered')
    context = {'academies_list': academies_list}

    return render(request, 'AcademyApp/academies.html', context)


def academy(request, academy_id):
    try:
        acdmy = Academy.objects.get(pk=academy_id)
        context = {'acdmy': acdmy}
    except Academy.DoesNotExist:
        raise Http404("Academy does not exist")
    return render(request, 'AcademyApp/academy.html', context)


def academiesjson(request):
    return HttpResponse(serializers.serialize('json', Academy.objects.all()))


def academiesxml(request):
    return HttpResponse(serializers.serialize('xml', Academy.objects.all()))