from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.login_page, name='login_page'),
    url(r'^auth', views.auth_user, name='auth'),
    url(r'^index$', views.index, name='index'),

    # ex: /AcademyApp/get/list
    url(r'^students/get/list$', views.students, name='getStudents'),
    # ex: /AcademyApp/get/5
    url(r'^students/get/(?P<student_id>[0-9]+)', views.student, name='getStudent'),
    # ex: /AcademyApp/get/list.json
    url(r'^students/get/list.json$', views.studentsjson, name='getStudentsJson'),
    # ex: /AcademyApp/get/list.xml
    url(r'^students/get/list.xml$', views.studentsxml, name='getStudentsXML'),

    url(r'^teachers/get/list$', views.teachers, name='getTeachers'),
    url(r'^teachers/get/(?P<teacher_id>[0-9]+)', views.teacher, name='getTeacher'),
    url(r'^teachers/get/list.json$', views.teachersjson, name='getTeachersJson'),
    url(r'^teachers/get/list.xml$', views.teacherssxml, name='getTeachersXML'),

    url(r'^academies/get/list$', views.academies, name='getAcademies'),
    url(r'^academies/get/(?P<academy_id>[0-9]+)', views.academy, name='getAcademy'),
    url(r'^academies/get/list.json$', views.academiesjson, name='getAcademiesJson'),
    url(r'^academies/get/list.xml$', views.academiesxml, name='getAcademiesXML'),
]