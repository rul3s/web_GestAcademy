from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse


class Student(models.Model):
    name = models.CharField(max_length=50, default="std")
    direction = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    telephone = models.CharField(max_length=9)
    email = models.EmailField()
    academy = models.ForeignKey('Academy', blank=True, null=True)
    registered = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})


class Teacher(models.Model):
    name = models.CharField(max_length=60)
    direction = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    telephone = models.CharField(max_length=9)
    email = models.EmailField()
    registered = models.DateTimeField(default=datetime.now())
    academy = models.ForeignKey('Academy', blank=True, null=True)
    author = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'pk': self.pk})


class Academy(models.Model):
    name = models.CharField(max_length=60)
    direction = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    registered = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'pk': self.pk})


class TeacherStudents(models.Model):
    registered = models.DateTimeField(default=datetime.now())
    teacher = models.ForeignKey('Teacher')
    student = models.ForeignKey('Student')

    def __str__(self):
        return str(self.registered) + " " + self.teacher.name + " " + self.student.name


class Review(models.Model):
    RATING_CHOICES = ((1,	'one'),	(2,	'two'),	(3,	'three'),	(4,	'four'),	(5,	'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)',	blank=False,	default=3,	choices=RATING_CHOICES)
    comment = models.TextField(blank=True,	null=True)
    user = models.ForeignKey(User,	default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class TeacherReview(Review):
    teacher = models.ForeignKey(Teacher)

class AcademyReview(Review):
    academy = models.ForeignKey(Academy)
