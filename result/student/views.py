from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from student.preprocesssing import  get_section_list
from student.add_to_DB import split_data
from .add_to_DB import split_data_student
from student.back_log_handler import split_data_backlog
from .analysis.sem_analysis import get_subject_analysis_data
from .analysis.sect_analysis import section_analysis
from student.preprocesssing import get_subj_list, get_subject_analysis, get_transformed_data
from .models import BacklogData, Batch, Branch, Performance, Regulation, Semester, Student, Subjects
import os
import pandas as pd
# Create your views here.


def index(request):
    # print("hi")
    # if request.method == 'POST':
    #     if "excel" in request.FILES:
    #         user = request.FILES["excel"]
    #         ex = Semester(file=user)
    #         ex.save()
    #         data = pd.read_excel(user)
    #         title = get_subj_list(data,6)
    #         di = get_transformed_data(data)
    #         d1 = di[0][title[-1]]
    #         print(d1[d1["Roll"] == "20135A0514"])
    #         print(title[-1])
    sem = Semester.objects.all()
    # # subj = Subjects.objects.filter(name="DISCRETE MATHEMATICAL STRUCTURES")
    # get_subject_analysis(sem,"DISCRETE MATHEMATICAL STRUCTURES")
    
    context  = {
        'sem':sem,
    }
    return render(request,"base.html",context) 

def upload(request):
    sem = Semester.objects.all()
    reg = Regulation.objects.all()
    branch = Branch.objects.all()
    batch = Batch.objects.all()
    context = {
        'sem':sem,
        'branch':branch,
        "reg":reg,
        'batch':batch,
    }
    
    return render(request,"upload_excel.html",context)



def backlogupload(request):
    sem = Semester.objects.all()
    reg = Regulation.objects.all()
    branch = Branch.objects.all()
    batch = Batch.objects.all()
    context = {
        'sem':sem,
        'branch':branch,
        "reg":reg,
        'batch':batch
    }
    
    return render(request,"back_log.html",context)

def backlogdata(request):
    if request.method == "POST":
        reg = request.POST.get("reg")
        branch = request.POST.get("branch")
        batch = request.POST.get("batch")
        sem = request.POST.get("sem")
        bra = Branch.objects.get(id=branch)
        reg = Regulation.objects.get(id=reg)
        batch = Batch.objects.get(id=batch)
        sem = Semester.objects.get(id=sem)
        backdata = BacklogData(sem=sem,regulation=reg,branch=bra,batch=batch)
        backdata.save()
        # backdata = BacklogData.objects.get(id=backdata.id)
        
        if "file" in request.FILES:
            data = request.FILES['file']
            backdata.file = data
            backdata.save()
        backdata.save()
        
        split_data_backlog(data,sem.id)

    sem = Semester.objects.all()
    reg = Regulation.objects.all()
    branch = Branch.objects.all()
    batch = Batch.objects.all()
    context = {
        'sem':sem,
        'branch':branch,
        "reg":reg,
        'batch':batch
    }
    
    return render(request,"back_log.html",context)


def data(request):
    if request.method == "POST":
        reg = request.POST.get("reg")
        branch = request.POST.get("branch")
        name = request.POST.get("name")
        # type = request.POST.get("type")
        no_of_subject = request.POST.get("no_of_subject")
        batch = request.POST.get('batch')
        bra = Branch.objects.get(id=branch)
        reg = Regulation.objects.get(id=reg)
        batch = Batch.objects.get(id=batch)
        if Semester.objects.filter(branch=bra,batch=batch,regulation=reg,name=name).exists():
            pass
        else:
            sem = Semester(name=name,branch=bra,no_of_subject=no_of_subject,regulation=reg,batch=batch)
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
    batch = Batch.objects.all()
    context = {
        'sem':sem,
        'branch':branch,
        "reg":reg,
        "batch":batch
    }
    return render(request,"upload_excel.html",context)  





def get_sem_analysis(request,sem_id):
    if Semester.objects.filter(id=sem_id).exists():
        sem = Semester.objects.get(id=sem_id)
        return JsonResponse(get_subject_analysis_data(sem))
    
    
    
    
def get_sect_analysis(request, sem_id):
    if Semester.objects.filter(id=sem_id).exists():
        sem = Semester.objects.get(id=sem_id)
        reg = Regulation.objects.get(id=sem.regulation.id)
        batch = Batch.objects.get(id=sem.batch.id)
        branch = Branch.objects.get(id=sem.branch.id)
        if Student.objects.filter(regulation=reg, batch=batch,branch=branch).exists():
            students = Student.objects.all().filter(regulation=reg, batch=batch,branch=branch)
            sect_list = get_section_list(students)
            # print(sect_list)
            data = {}
            for i in list(sect_list.keys()):  
                analyse = section_analysis(i,reg,batch,branch,sem,students)
                data[f"Section: {i}"] = analyse
            return JsonResponse(data)
    
    return HttpResponse("hi")
        
        



def student_detail(request):
    if request.method == "POST":
        reg = request.POST.get("reg")
        branch = request.POST.get("branch")
        batch = request.POST.get("batch")
        bra = Branch.objects.get(id=branch)
        reg = Regulation.objects.get(id=reg)
        batch = Batch.objects.get(id=batch)
        # students = Student.objects.all().filter(regulation=reg,branch=bra, batch=batch)
        # backdata = BacklogData.objects.get(id=backdata.id)
        
        if "file" in request.FILES:
            data = request.FILES['file']
            split_data_student(data, bra,reg,batch)
            
            
        
        # split_data_backlog(data,sem.id).\
    
    
    reg = Regulation.objects.all()
    batch = Batch.objects.all()
    branch = Branch.objects.all()
    
    context = {
        'regs': reg,
        'batch': batch,
        'branch': branch,
    }
    
    return render(request, "student.html",context)