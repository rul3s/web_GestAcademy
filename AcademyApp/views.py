from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello world. You're at the Academy index.")


def liststudents(request):
    return HttpResponse("Hello world. You're at the Students list.")


def listteachers(request):
    return HttpResponse("Hello world. You're at the Teachers list.")


def listacademies(request):
    return HttpResponse("Hello world. You're at the Academies list.")

