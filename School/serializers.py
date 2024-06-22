from rest_framework import serializers
from School.models import School, Branch, Teacher, Parent, Student, Classes

class SchoolSerializer(serializers.ModelSerializer) :
    
    class Meta :
        fields = '__all__'
        model = School

class BranchSerializer(serializers.ModelSerializer) :
    
    class Meta :
        fields = '__all__'
        model = Branch

class TeacherSerializer(serializers.ModelSerializer) :
    
    class Meta :
        fields = '__all__'
        model = Teacher

class ParentSerializer(serializers.ModelSerializer) :
    
    class Meta :
        fields = '__all__'
        model = Parent

class StudentSerializer(serializers.ModelSerializer) :
    
    class Meta :
        fields = '__all__'
        model = Student

class ClassesSerializer(serializers.ModelSerializer) :
    
    class Meta :
        fields = '__all__'
        model = Classes
        