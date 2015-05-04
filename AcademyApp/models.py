from django.db import models
import datetime

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=60)
    direction = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    telephone = models.CharField(max_length=9)
    email = models.EmailField()
    academy = models.ForeignKey('Academy', blank=True, null=True)

    def __str__(self):
        return self.name


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





