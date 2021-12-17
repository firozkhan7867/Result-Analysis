from django.contrib import admin
from .models import Branch, Regulation, Semester, Student, Subjects
# Register your models here.
admin.site.register([Semester,Student,Branch,Regulation,Subjects])
