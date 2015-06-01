from django import forms
from django.forms import ModelForm
from django.views.generic.edit import UpdateView
from AcademyApp.models import *

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class StdForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name',
                  'direction',
                  'city', 'telephone',
                  'email',
                  'academy',
                  'registered'
                  ]


class TchrForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['name',
                  'direction',
                  'city', 'telephone',
                  'email',
                  'academy',
                  'registered'
                  ]

class AcdmyForm(ModelForm):
    class Meta:
        model = Academy
        fields = ['name',
                  'direction',
                  'city',
                  'registered'
                  ]

