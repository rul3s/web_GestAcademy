from django.shortcuts import render
from django.http import HttpResponse
from models import *

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
    output = "*************Students LIST*************<br>"
    students_list = Student.objects.order_by('registered')
    output += ', '.join([s.name for s in students_list])
    return HttpResponse(output)


def student(request, student_id):
    return HttpResponse("Hello world. You're looking for student %s" % student_id)


def teachers(request):
    output = "*************Teachers LIST*************<br>"
    teachers_list = Teacher.objects.order_by('registered')
    output += ', '.join([t.name for t in teachers_list])
    return HttpResponse(output)


def teacher(request, teacher_id):
    return HttpResponse("Hello world. You're looking for teacher %s " % teacher_id)


def academies(request):
    output = "*************Academies LIST*************<br>"
    academies_list = Academy.objects.order_by('registered')
    output += ', '.join([a.name for a in academies_list])
    return HttpResponse(output)


def academy(request, academy_id):
    return HttpResponse("Hello world. You're looking for academy %s" % academy_id)