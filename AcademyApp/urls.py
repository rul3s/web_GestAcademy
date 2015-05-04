from django.conf.urls import url

from . import views

urlpatterns = [
    # regularExpr, view, keyword args, name
    # ex: /AcademyApp/
    url(r'^$', views.index, name='index'),
    # ex: /AcademyApp/students
    url('students', views.liststudents, name='liststudents'),
    url('teachers', views.listteachers, name='listteachers'),
    url('academies', views.listacademies, name='listacademies'),
]