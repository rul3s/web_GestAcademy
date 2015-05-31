from django import forms
from django.forms import ModelForm
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

