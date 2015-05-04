from django.contrib import admin
from .models import *

# Register your models here.

'''
class StudentAdmin(admin.ModelAdmin):
    fields = ['name', 'direction']
'''

admin.site.register(Academy)
admin.site.register(Teacher)
admin.site.register(Student)
# admin.site.register(Student, StudentAdmin)
admin.site.register(TeacherStudents)





