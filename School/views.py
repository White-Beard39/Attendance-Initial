from django.shortcuts import render
from rest_framework import viewsets
from School.models import School, Branch, Teacher, Parent, Student
from School.serializers import SchoolSerializer, BranchSerializer, TeacherSerializer, StudentSerializer, ParentSerializer
# Create your views here.

class SchoolViewSet (viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer = SchoolSerializer

class BranchViewSet (viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer = BranchSerializer

class TeacherViewSet (viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer = TeacherSerializer

class ParentViewSet (viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer = ParentSerializer

class StudentViewSet (viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer = StudentSerializer