from views import *
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

urlpatterns = [

    url(r'^$', login_required(index), name='index'),
    url(r'^index$', login_required(index), name='index'),
    url(r'^login$', login_view, name='login_view'),
    url(r'^logout$', logout_view, name='logout_view'),
    url(r'^auth$', auth_user, name='auth'),

    # Student detail: /AcademyApp/get/student/1
    url(r'^get/student/(?P<pk>\d+)/$',              login_required(StudentDetail.as_view()),        name='student_detail'),
    # Student list: /AcademyApp/get/student/list
    url(r'^get/student/list$',                      login_required(StudentList.as_view()),          name='student_list'),
    # Create Student: /AcademyApp/post/student
    url(r'^post/student$',                          login_required(StudentCreate.as_view()),        name='student_create'),
    # Modify Student: /AcademyApp/update/student/1
    url(r'^update/student/(?P<pk>[0-9]+)/$',        login_required(StudentUpdate.as_view()),        name='student_update'),
    # Delete Student: /AcademyApp/delete/student/1
    url(r'^delete/student/(?P<pk>[0-9]+)/$',        login_required(StudentDelete.as_view()),        name='student_delete'),
    # Download Student list Json and XML: /AcademyApp/get/student/list.json
    url(r'^get/student/list.json$',                 login_required(student_list_json),              name='student_list_json'),
    # Download Student list Json and XML: /AcademyApp/get/student/list.xml
    url(r'^get/student/list.xml$',                  login_required(student_list_xml),               name='student_list_xml'),


    url(r'^get/teacher/(?P<pk>\d+)/$',              login_required(TeacherDetail.as_view()),        name='teacher_detail'),
    url(r'^get/teacher/list$',                      login_required(TeacherList.as_view()),          name='teacher_list'),
    url(r'^post/teacher$',                          login_required(TeacherCreate.as_view()),        name='teacher_create'),
    url(r'^update/teacher/(?P<pk>[0-9]+)/$',        login_required(TeacherUpdate.as_view()),        name='teacher_update'),
    url(r'^delete/teacher/(?P<pk>[0-9]+)/$',        login_required(TeacherDelete.as_view()),        name='teacher_delete'),
    url(r'^get/teacher/list.json$',                 login_required(teacher_list_json),              name='teacher_list_json'),
    url(r'^get/teacher/list.xml$',                  login_required(teacher_list_xml),               name='teacher_list_xml'),
    url(r'^post/teacher/(?P<pk>\d+)/reviews/create/$',
                                                    login_required(teacher_review),	                name='teacher_review_create'),


    url(r'^get/academy/(?P<pk>\d+)/$',              login_required(AcademyDetail.as_view()),        name='academy_detail'),
    url(r'^get/academy/list$',                      login_required(AcademyList.as_view()),          name='academy_list'),
    url(r'^post/academy$',                          login_required(AcademyCreate.as_view()),        name='academy_create'),
    url(r'^update/academy/(?P<pk>[0-9]+)/$',        login_required(AcademyUpdate.as_view()),        name='academy_update'),
    url(r'^delete/academy/(?P<pk>[0-9]+)/$',        login_required(AcademyDelete.as_view()),        name='academy_delete'),
    url(r'^get/academy/list.json$',                 login_required(academy_list_json),              name='academy_list_json'),
    url(r'^get/academy/list.xml$',                  login_required(academy_list_xml),               name='academy_list_xml'),
    url(r'^post/academy/(?P<pk>\d+)/reviews/create/$',
                                                    login_required(academy_review),	                name='academy_review_create'),
]


'''
    url(r'^api/$', 'api_root'),
    url(r'^api/academies/$',                        APIAcademyList.as_view(),                       name='academy-list'),
    url(r'^api/academies/(?P<pk>\d+)/$',            APIAcademyDetail.as_view(),                     name='academy-detail'),
    url(r'^api/teachers/$',                         APITeacherList.as_view(),                       name='teacher-list'),
    url(r'^api/teachers/(?P<pk>\d+)/$',             APITeacherDetail.as_view(),                     name='teacher-detail'),
    url(r'^api/academyreviews/$',	                APIAcademyReviewList.as_view(),                 name='academyreview-list'),
    url(r'^api/academyreviews/(?P<pk>\d+)/$',	    APIAcademyReviewDetail.as_view(),               name='academyreview-detail'),
    url(r'^api/teacherreviews/$',	                APITeacherReviewList.as_view(),                 name='teacherreview-list'),
    url(r'^api/teacherreviews/(?P<pk>\d+)/$',	    APITeacherReviewDetail.as_view(),               name='teacherreview-detail'),
'''