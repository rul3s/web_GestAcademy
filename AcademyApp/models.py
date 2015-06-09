from django.db import models
import datetime
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50, default="std")
    direction = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    telephone = models.CharField(max_length=9)
    email = models.EmailField()
    academy = models.ForeignKey('Academy', blank=True, null=True)
    registered = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = (
            ("add_std", "Can create new student"),
            ("change_std", "Can change existing student"),
            ("remove_std", "Can remove existing student"),
        )


class Teacher(models.Model):
    name = models.CharField(max_length=60)
    direction = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    telephone = models.CharField(max_length=9)
    email = models.EmailField()
    registered = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name

    academy = models.ForeignKey('Academy', blank=True, null=True)


class Academy(models.Model):
    name = models.CharField(max_length=60)
    direction = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    registered = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name


class TeacherStudents(models.Model):
    registered = models.DateTimeField(default=datetime.datetime.now())
    teacher = models.ForeignKey('Teacher')
    student = models.ForeignKey('Student')

    def __str__(self):
        return str(self.registered) + " " + self.teacher.name + " " + self.student.name
