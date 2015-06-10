'''
# Modify Student: /AcademyApp/update/student/1
url(r'^update/student/(?P<pk>[0-9]+)/$', edit_std, name='student_update'),
# Delete Student: /AcademyApp/delete/student/1
url(r'^delete/student/(?P<pk>[0-9]+)/$', StudentDelete.as_view(), name='student_remove'),






    url(r'^get/teacher/(?P<pk>\d+)/$', TeacherDetail.as_view(), name='teacher_detail'),
    url(r'^get/teacher/list$', teacher_list, name='teacher_list'),
    url(r'^get/teacher/list.json$', teacher_list_json, name='teacher_list_json'),
    url(r'^get/teacher/list.xml$', teacher_list_xml, name='teacher_list_xml'),
    url(r'^post/teacher$', TeacherCreate.as_view(success_url=reverse_lazy('index')), name='teacher_create'),
    url(r'^update/teacher/(?P<pk>[0-9]+)/$', TeacherUpdate.as_view(), name='teacher_update'),
    url(r'^delete/teacher/(?P<pk>[0-9]+)/$', TeacherDelete.as_view(), name='teacher_delete'),

    url(r'^get/academy/(?P<pk>\d+)/$', AcademyDetail.as_view(), name='academy_detail'),
    url(r'^get/academy/list$', academy_list, name='academy_list'),
    url(r'^get/teacher/list.json$', academy_list_json, name='academy_list_json'),
    url(r'^get/teacher/list.xml$', academy_list_xml, name='academy_list_xml'),
    url(r'^post/academy$', AcademyCreate.as_view(success_url=reverse_lazy('index')), name='academy_create'),
    url(r'^update/student/(?P<pk>[0-9]+)/$', AcademyUpdate.as_view(), name='academy_update'),
    url(r'^delete/student/(?P<pk>[0-9]+)/$', AcademyDelete.as_view(), name='academy_delete'),




'''
