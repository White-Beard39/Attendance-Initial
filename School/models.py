from django.db import models

class School(models.Model):
    name=models.CharField(max_length=512)
    has_branches=models.BooleanField(default=False)
    founded_on=models.DateField()

    def __str__(self):
        return self.name
    
class Branch(models.Model):
    name=models.CharField(max_length=512)
    school=models.ForeignKey(School, on_delete=models.CASCADE)
    established_on=models.DateField()
    location=models.CharField(max_length=128)

    def __str__(self):
        return self.name
    
class Parent(models.Model):
    school=models.ForeignKey(School, on_delete=models.CASCADE,related_name='parents')
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    phone_number=models.CharField(max_length=10)
    watsapp_number=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    school=models.ForeignKey(School, on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    phone_number=models.CharField(max_length=10)
    email=models.EmailField()
    gender=models.CharField(max_length=1)
    age=models.IntegerField()

    def __str__(self):
        return self.name

    
class Student(models.Model):
    school=models.ForeignKey(School, on_delete=models.CASCADE)
    parent=models.ForeignKey(Parent, on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    roll_number=models.IntegerField()
    
    def __str__(self): 
        return self.name
