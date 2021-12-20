from django.db import models
import os

# Create your models here.

def path_and_rename(instance, filename):
    upload_to = "Excel/"
    ext = filename.split('.')[-1]
    if instance.name:
        filename = f"files/{instance.regulation}/{instance.branch}/{instance.name}.{ext}"
    return os.path.join(upload_to, filename)



class Branch(models.Model):
    branches = models.CharField(max_length=50)
    
    def __str__(self):
        return self.branches
    
    class Meta:
        verbose_name_plural = "Branches"
    
    
    
class Regulation(models.Model):
    regulation = models.CharField(max_length=50,unique=True)
    year = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.regulation} for year {self.year}"


class Semester(models.Model):
    name = models.CharField(max_length=10)
    no_of_subject = models.IntegerField()
    regulation = models.ForeignKey(Regulation,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    # subject = models.ManyToManyField(Subjects,blank=True)
    year = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=path_and_rename, verbose_name="Excel FIle", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Semesters"
    
    # def all_subject(self):
    #     subj = Subjects.objects.all().filter(sem=self.id)
    #     return subj
    
class Student(models.Model):
    roll = models.CharField(max_length=15,unique=True)
    name = models.CharField(max_length=120,blank=True)
    # gender = models.CharField(c)
    regulation = models.ForeignKey(Regulation,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    sem = models.ManyToManyField(Semester)
    section = models.IntegerField(default=10,blank=True)

    def __str__(self):
        return self.roll
    
    def sems(self):
        sems = Semester.objects.all().filter(regulation=self.regulation)
        return sems
    
    
    class Meta:
        verbose_name_plural = "Students"
    

class Subjects(models.Model):
    roll = models.ForeignKey(Student,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    regulation = models.ForeignKey(Regulation,on_delete=models.CASCADE)
    sem = models.ForeignKey(Semester,on_delete=models.CASCADE)
    credit = models.FloatField()
    result = models.CharField(max_length=20,blank=True)
    attendance = models.CharField(max_length=5,blank=True)
    grade = models.CharField(max_length=5,blank=True)
    cgpa = models.FloatField()
    fail = models.BooleanField(default=False)
    # semester = models.ManyToManyField(Semester)
    def __str__(self):
        return f"{self.name} of  {self.roll.roll} during {self.sem.name} got cgpa of {self.cgpa}"
    
    class Meta:
        verbose_name_plural = "Subjects"
        
    
class Performance(models.Model):
    roll = models.ForeignKey(Student,on_delete=models.CASCADE)
    regulation = models.ForeignKey(Regulation, on_delete=models.CASCADE)
    sem = models.ForeignKey(Semester,on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subjects)
    registered = models.IntegerField(blank=True)
    no_of_pass = models.IntegerField(blank=True)
    TCR = models.FloatField(blank=True)
    TCP = models.FloatField(blank=True)
    SCGPA = models.FloatField(blank=True)
    
    def __str__(self):
        return f"{self.roll} got SCGPA of {self.SCGPA} for {self.sem.name} semester"
    
    
    
    
    