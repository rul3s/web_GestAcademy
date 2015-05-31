from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^your-name$', views.get_name, name='get_name'),

    url(r'^$', views.login_view, name='login_view'),
    url(r'^logout$', views.logout_view, name='logout_view'),
    url(r'^auth', views.auth_user, name='auth'),
    url(r'^index$', views.index, name='index'),

    # ex: /AcademyApp/get/list
    url(r'^students/post$', views.add_std, name='add_std'),
    url(r'^students/update(?P<student_id>[0-9]+)', views.edit_std, name='editStudent'),
    url(r'^students/get/list$', views.students, name='getStudents'),
    url(r'^students/get/(?P<student_id>[0-9]+)', views.student, name='getStudent'),
    url(r'^students/get/list.json$', views.studentsjson, name='getStudentsJson'),
    url(r'^students/get/list.xml$', views.studentsxml, name='getStudentsXML'),

    url(r'^teachers/get/list$', views.teachers, name='getTeachers'),
    url(r'^teachers/get/(?P<teacher_id>[0-9]+)', views.teacher, name='getTeacher'),
    url(r'^teachers/get/list.json$', views.teachersjson, name='getTeachersJson'),
    url(r'^teachers/get/list.xml$', views.teacherssxml, name='getTeachersXML'),

    #url(r'^academies/post', views.addacademy, name='addAcademy'),
    #url(r'^academies/update/(?P<academy_id>[0-9]+)', views.updateacademy, name='updateAcademy'),
    #url(r'^academies/delete/(?P<academy_id>[0-9]+)', views.deleteacademy, name='deleteAcademy'),
    url(r'^academies/get/list$', views.academies, name='getAcademies'),
    url(r'^academies/get/(?P<academy_id>[0-9]+)', views.academy, name='getAcademy'),
    url(r'^academies/get/list.json$', views.academiesjson, name='getAcademiesJson'),
    url(r'^academies/get/list.xml$', views.academiesxml, name='getAcademiesXML'),
]