from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.template import RequestContext, loader

# Create your views here.


def index(request):
    output = "*************LIST OF DIFERENT OBJECTS***************<br>"

    output += "<br><br>Academies:<br>"
    academies_list = Academy.objects.order_by('registered')
    output += ', '.join([a.name for a in academies_list])

    output += "<br><br>Teachers:<br>"
    teachers_list = Teacher.objects.order_by('registered')
    output += ', '.join([t.name for t in teachers_list])

    output += "<br><br>Students:<br>"
    students_list = Student.objects.order_by('registered')
    output += ', '.join([s.name for s in students_list])
    return HttpResponse(output)


def students(request):
    latest_students_list = Student.objects.order_by('registered')
    template = loader.get_template('AcademyApp/students.html')
    context = RequestContext(request, {
        'latest_students_list': latest_students_list,
    })

    return HttpResponse(template.render(context))


def student(request, student_id):
    return HttpResponse("Hello world. You're looking for student %s" % student_id)


def teachers(request):
    teachers_list = Teacher.objects.order_by('registered')
    template = loader.get_template('AcademyApp/teachers.html')
    context = RequestContext(request, {
        'teachers_list': teachers_list,
    })

    return HttpResponse(template.render(context))


def teacher(request, teacher_id):
    return HttpResponse("Hello world. You're looking for teacher %s " % teacher_id)


def academies(request):
    academies_list = Academy.objects.order_by('registered')
    template = loader.get_template('AcademyApp/academies.html')
    context = RequestContext(request, {
        'academies_list': academies_list,
    })

    return HttpResponse(template.render(context))


def academy(request, academy_id):
    return HttpResponse("Hello world. You're looking for academy %s" % academy_id)