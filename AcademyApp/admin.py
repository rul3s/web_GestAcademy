from django.contrib import admin
from .models import *

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'direction', 'city', 'telephone', 'email', 'academy']}),
        ('Registered on', {'fields': ['registered'], 'classes': ['collapse']})
    ]

    list_display = ('name', 'registered', 'city')


admin.site.register(Academy)
admin.site.register(Teacher)
# admin.site.register(Student)
admin.site.register(Student, StudentAdmin)
admin.site.register(TeacherStudents)





