from django.contrib import admin
from .models import Attempt, BacklogData, BacklogSubject, Batch, Branch, Performance, Regulation, Semester, Student, Subjects
# Register your models here.
admin.site.register([Semester,Student,Branch,Regulation,Subjects,Performance, BacklogSubject ,Attempt, Batch,BacklogData])
