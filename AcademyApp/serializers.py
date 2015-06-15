from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Academy, AcademyReview, Teacher, TeacherReview, Student

class AcademySerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='academy-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Academy

class AcademyReviewSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='academy-review')
    user = CharField(read_only=True)

    class Meta:
        model = AcademyReview

class TeacherSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='teacher-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Teacher

class TeacherReviewSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='teacher-review')
    user = CharField(read_only=True)

    class Meta:
        model = TeacherReview

class StudentSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='student-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Student
