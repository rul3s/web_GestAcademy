from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import *
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from serializers import	AcademySerializer, AcademyReviewSerializer,	TeacherSerializer, TeacherReviewSerializer, StudentSerializer
from rest_framework	import	generics
from rest_framework.decorators	import	api_view

def login_view(request):
    template = loader.get_template('AcademyApp/login.html')
    return HttpResponse(template.render())

def logout_view(request):
    logout(request)
    return render(request, 'AcademyApp/logout.html', {})

def auth_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return redirect("index")

        else:
            # Return a 'disabled account' error message
            template = loader.get_template('AcademyApp/error.html')
    else:
        # Return an 'invalid login' error message.
        template = loader.get_template('AcademyApp/error.html')

    return HttpResponse(template.render())

def index(request):
    return render(request, 'AcademyApp/index.html', {})

########################################## STUDENTS ######################################################
def student_list_json(request):
    response = HttpResponse(serializers.serialize('json', Student.objects.all()), content_type='text/plain', charset='utf8')
    response['Content-Disposition'] = 'attachment; filename=students.json'
    return response

def student_list_xml(request):
    response = HttpResponse(serializers.serialize('xml', Student.objects.all()), content_type='text/plain', charset='utf8')
    response['Content-Disposition'] = 'attachment; filename=students.xml'
    return response

class StudentDetail(DetailView):
    model = Student
    template_name = 'AcademyApp/student_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)
        return context

class StudentList(ListView):
    model = Student
    template_name = 'AcademyApp/student_list.html'

class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'AcademyApp/form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(StudentCreate, self).form_valid(form)

class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'AcademyApp/form.html'
    success_url = reverse_lazy('student_list')

class StudentDelete(DeleteView):
    model = Student
    template_name = "AcademyApp/confirm_delete.html"
    success_url = reverse_lazy('student_list')

class APIStudentList(generics.ListCreateAPIView):
    model = Student
    serializer_class = StudentSerializer

class APIStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    model =	Student
    serializer_class = StudentSerializer

########################################## TEACHERS ######################################################
def teacher_list_json(request):
    response = HttpResponse(serializers.serialize('json', Teacher.objects.all()), content_type='text/plain', charset='utf8')
    response['Content-Disposition'] = 'attachment; filename=teachers.json'
    return response

def teacher_list_xml(request):
    response = HttpResponse(serializers.serialize('xml', Teacher.objects.all()), content_type='text/plain', charset='utf8')
    response['Content-Disposition'] = 'attachment; filename=teachers.xml'
    return response

class TeacherDetail(DetailView):
    model = Teacher
    template_name = 'AcademyApp/teacher_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherDetail, self).get_context_data(**kwargs)
        return context

class TeacherList(ListView):
    model = Teacher
    template_name = 'AcademyApp/teacher_list.html'

class TeacherCreate(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'AcademyApp/form.html'
    success_url = reverse_lazy('teacher_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TeacherCreate, self).form_valid(form)

class TeacherUpdate(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'AcademyApp/form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherDelete(DeleteView):
    model = Teacher
    template_name = "AcademyApp/confirm_delete.html"
    success_url = reverse_lazy('teacher_list')

def teacher_review(request,	pk):
    teacher = get_object_or_404(Teacher,	pk=pk)
    review = TeacherReview(rating=request.POST['rating'], comment=request.POST['comment'], user=request.user, teacher=teacher)
    review.save()
    return HttpResponseRedirect(reverse('teacher_detail',	args=(teacher.id,)))

class APITeacherList(generics.ListCreateAPIView):
    model = Teacher
    serializer_class = TeacherSerializer

class APITeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Teacher
    serializer_class = TeacherSerializer

class APITeacherReviewList(generics.ListCreateAPIView):
    model = TeacherReview
    serializer_class = TeacherReviewSerializer

class APITeacherReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    model = TeacherReview
    serializer_class = TeacherReviewSerializer

########################################## ACADEMIES ######################################################
def academy_list_json(request):
    response = HttpResponse(serializers.serialize('json', Academy.objects.all()), content_type='text/plain', charset='utf8')
    response['Content-Disposition'] = 'attachment; filename=academies.json'
    return response

def academy_list_xml(request):
    response = HttpResponse(serializers.serialize('xml', Academy.objects.all()), content_type='text/plain', charset='utf8')
    response['Content-Disposition'] = 'attachment; filename=academies.xml'
    return response

class AcademyDetail(DetailView):
    model = Academy
    template_name = 'AcademyApp/academy_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AcademyDetail, self).get_context_data(**kwargs)
        return context

class AcademyList(ListView):
    model = Academy
    template_name = 'AcademyApp/academy_list.html'

class AcademyCreate(CreateView):
    model = Academy
    form_class = AcademyForm
    template_name = 'AcademyApp/form.html'
    success_url = reverse_lazy('academy_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AcademyCreate, self).form_valid(form)

class AcademyUpdate(UpdateView):
    model = Academy
    form_class = AcademyForm
    template_name = 'AcademyApp/form.html'
    success_url = reverse_lazy('academy_list')

class AcademyDelete(DeleteView):
    model = Academy
    template_name = "AcademyApp/confirm_delete.html"
    success_url = reverse_lazy('academy_list')

def academy_review(request,	pk):
    academy = get_object_or_404(Academy, pk=pk)
    review = AcademyReview(rating=request.POST['rating'], comment=request.POST['comment'], user=request.user, academy=academy)
    review.save()
    return HttpResponseRedirect(reverse('academy_detail',	args=(academy.id,)))

class APIAcademyList(generics.ListCreateAPIView):
    model = Academy
    serializer_class = AcademySerializer

class APIAcademyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Academy
    serializer_class = AcademySerializer

class APIAcademyReviewList(generics.ListCreateAPIView):
    model = AcademyReview
    serializer_class = AcademyReviewSerializer

class APIAcademyReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    model = AcademyReview
    serializer_class = AcademyReviewSerializer
