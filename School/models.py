from django.db import models

class School(models.Model):
    name=models.CharField(max_length=512)
    has_branches=models.BooleanField(default=False)
    founded_on=models.DateField()

    def __str__(self):
        return self.name
    
class Branch(models.Model):
    school=models.ForeignKey(School, on_delete=models.CASCADE)
    established_on=models.DateField()
    location=models.CharField(max_length=128)

    def __str__(self):
        return self.location
    
class Parent(models.Model):
    school=models.ForeignKey(School, on_delete=models.DO_NOTHING,related_name='parents')
    branch=models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=64)
    phone_number=models.CharField(max_length=10)
    watsapp_number=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    school=models.ForeignKey(School, on_delete=models.DO_NOTHING)
    branch=models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=64)
    phone_number=models.CharField(max_length=10)
    email=models.EmailField()
    gender=models.CharField(max_length=1)
    age=models.IntegerField()

    def __str__(self):
        return self.name

    
class Student(models.Model):
    school=models.ForeignKey(School, on_delete=models.DO_NOTHING)
    parent=models.ForeignKey(Parent, on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    roll_number=models.IntegerField()
    
    def __str__(self): 
        return self.name

class Classes(models.Model):
    class_choices = [ ("LKG","LKG"),("UKG","class UKG"),("1","class 1"),("2","class 2"),("3","class 3"),("4","class 4"),("5","class 5"),("6","class 6"),("7","class 7"),("8","class 8"),("9","class 9"),("10","class 10"),]
    class_no = models.CharField(max_length=3)
    section = models.CharField(max_length=1)
    class_teacher = models.OneToOneField(Teacher, on_delete=models.DO_NOTHING)
    class_student = models.ManyToManyField(Student)

    def __str__ (self):
        return f"{self.class_no} {self.section}"