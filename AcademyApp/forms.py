from django.forms import ModelForm
from AcademyApp.models import *

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ('registered', 'author')


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = ('registered', 'author')

class AcademyForm(ModelForm):
    class Meta:
        model = Academy
        exclude = ('registered', 'author')
