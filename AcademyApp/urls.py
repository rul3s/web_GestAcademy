from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.login_view, name='login_view'),
    url(r'^logout$', views.logout_view, name='logout_view'),
    url(r'^auth', views.auth_user, name='auth'),
    url(r'^index$', views.index, name='index'),

    # ex: /AcademyApp/get/list
    url(r'^students/post$', views.add_std, name='addStudent'),
    url(r'^students/update/(?P<student_id>[0-9]+)', views.edit_std, name='editStudent'),
    url(r'^students/delete/(?P<student_id>[0-9]+)', views.rem_std, name='remStudent'),
    url(r'^students/get/list$', views.students, name='getStudents'),
    url(r'^students/get/(?P<student_id>[0-9]+)', views.student, name='getStudent'),
    url(r'^students/get/list.json$', views.studentsjson, name='getStudentsJson'),
    url(r'^students/get/list.xml$', views.studentsxml, name='getStudentsXML'),

    url(r'^teachers/post$', views.add_tchr, name='addTeacher'),
    url(r'^teachers/update/(?P<teacher_id>[0-9]+)', views.edit_tchr, name='editTeacher'),
    url(r'^teachers/delete/(?P<teacher_id>[0-9]+)', views.rem_tchr, name='remTeacher'),
    url(r'^teachers/get/list$', views.teachers, name='getTeachers'),
    url(r'^teachers/get/(?P<teacher_id>[0-9]+)', views.teacher, name='getTeacher'),
    url(r'^teachers/get/list.json$', views.teachersjson, name='getTeachersJson'),
    url(r'^teachers/get/list.xml$', views.teacherssxml, name='getTeachersXML'),

    url(r'^teachers/post$', views.add_acdmy, name='addAcademy'),
    url(r'^teachers/update/(?P<academy_id>[0-9]+)', views.edit_acdmy, name='editAcademy'),
    url(r'^teachers/delete/(?P<academy_id>[0-9]+)', views.rem_acdmy, name='remAcademy'),
    url(r'^academies/get/list$', views.academies, name='getAcademies'),
    url(r'^academies/get/(?P<academy_id>[0-9]+)', views.academy, name='getAcademy'),
    url(r'^academies/get/list.json$', views.academiesjson, name='getAcademiesJson'),
    url(r'^academies/get/list.xml$', views.academiesxml, name='getAcademiesXML'),
]