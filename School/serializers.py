from rest_framework import serializers
from School.models import School, Branch, Teacher, Parent, Student

class SchoolSerializer(serializers.Serializer) :
    
    class Meta :
        fields = '__all__'
        model = School

class BranchSerializer(serializers.Serializer) :
    
    class Meta :
        fields = '__all__'
        model = Branch

class TeacherSerializer(serializers.Serializer) :
    
    class Meta :
        fields = '__all__'
        model = Teacher

class ParentSerializer(serializers.Serializer) :
    
    class Meta :
        fields = '__all__'
        model = Parent

class StudentSerializer(serializers.Serializer) :
    
    class Meta :
        fields = '__all__'
        model = Student
        