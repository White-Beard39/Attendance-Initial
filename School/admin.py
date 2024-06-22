from django.contrib import admin
from School.models import School, Branch, Teacher, Parent, Student, Classes


# admin.site.register(School)
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin) :
    list_display = ('id','name','has_branches','founded_on')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin) :
    list_display = ("id","school","established_on","location")

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin) :
    list_display = ("id","name","school","branch")

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin) :
    list_display = ("id","name","school","branch")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin) :
    list_display = ("id","name","school","roll_number")

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin) :
    list_display = ("id","class_no","section","class_teacher")