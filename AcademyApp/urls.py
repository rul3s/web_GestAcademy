from django.conf.urls import url

from . import views

urlpatterns = [
    # regularExpr, view, keyword args, name
    # ex: /AcademyApp/
    url(r'^$', views.index, name='index'),
    # ex: /AcademyApp/get/list
    url(r'^students/get/list$', views.students, name='getStudents'),
    # ex: /AcademyApp/get/5
    url(r'^students/get/(?P<student_id>[0-9]+)', views.student, name='getStudent'),
    url(r'^teachers/get/list$', views.teachers, name='getTeachers'),
    url(r'^teachers/get/(?P<teacher_id>[0-9]+)', views.teacher, name='getTeacher'),
    url(r'^academies/get/list$', views.academies, name='getAcademies'),
    url(r'^academies/get/(?P<academy_id>[0-9]+)', views.academy, name='getAcademie'),
]