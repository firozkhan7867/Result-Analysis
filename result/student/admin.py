from django.contrib import admin
from .models import Branch, Regulation, Semester, Student, Subjects,Performance
# Register your models here.
admin.site.register([Semester,Student,Branch,Regulation,Subjects, Performance])
