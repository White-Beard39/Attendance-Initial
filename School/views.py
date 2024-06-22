from django.shortcuts import render
from rest_framework import viewsets
from School.models import School, Branch, Teacher, Parent, Student, Classes
from School.serializers import SchoolSerializer, BranchSerializer, TeacherSerializer, StudentSerializer, ParentSerializer, ClassesSerializer
# Create your views here.

class SchoolViewSet (viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class BranchViewSet (viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class TeacherViewSet (viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ParentViewSet (viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class StudentViewSet (viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ClassesViewSet (viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class  = ClassesSerializer