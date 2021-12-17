from django.shortcuts import render
from numpy.core.function_base import add_newdoc
from student.add_to_DB import split_data

from student.preprocesssing import get_subj_list, get_transformed_data
from .models import Branch, Regulation, Semester
import os
import pandas as pd
# Create your views here.

def index(request):
    print("hi")
    if request.method == 'POST':
        if "excel" in request.FILES:
            user = request.FILES["excel"]
            ex = Semester(file=user)
            ex.save()
            data = pd.read_excel(user)
            title = get_subj_list(data,6)
            di = get_transformed_data(data)
            d1 = di[0][title[-1]]
            print(d1[d1["Roll"] == "20135A0514"])
            print(title[-1])
    return render(request,"base.html") 

def upload(request):
    sem = Semester.objects.all()
    reg = Regulation.objects.all()
    branch = Branch.objects.all()
    context = {
        'sem':sem,
        'branch':branch,
        "reg":reg,
    }
    
    return render(request,"upload_excel.html",context)


def data(request):
    if request.method == "POST":
        reg = request.POST.get("reg")
        branch = request.POST.get("branch")
        name = request.POST.get("name")
        no_of_subject = request.POST.get("no_of_subject")
        bra = Branch.objects.get(id=branch)
        reg = Regulation.objects.get(id=reg)
        sem = Semester(name=name,branch=bra,no_of_subject=no_of_subject,regulation=reg)
        sem.save()
        # sem.regulation.add(reg)
        
        if "file" in request.FILES:
            data = request.FILES['file']
            sem.file = data
            sem.save()
        sem.save()
        split_data(data,sem.id)
        
    sem = Semester.objects.all()
    reg = Regulation.objects.all()
    branch = Branch.objects.all()
    context = {
        'sem':sem,
        'branch':branch,
        "reg":reg,
    }
    return render(request,"upload_excel.html",context)  




