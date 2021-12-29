from django.db.models.fields import CharField
from django.http.response import HttpResponse
from student.add_to_DB import extract_name
from student.models import *
import pandas as pd
import numpy as np


def title_and_code(subj_list):
    titles = []
    code = []
    for sub in subj_list:
        d = extract_name(sub)
        titles.append(d[1])
        code.append(d[0])
    return [code, titles]


def subj_analysis_one_more(sem,batch,reg,branch,code,name):
    subs = Subjects.objects.all().filter(sem=sem,batch=batch,regulation=reg,branch=branch,code=code,name=name)
    fail_count = 0
    num_of_student = 0
    pass_count = 0
    for sub in subs:
        if sub.fail == True:
            fail_count += 1
        else:
            pass_count +=1
            
        num_of_student +=1
    return {"fail":fail_count,"total_student":num_of_student,"passed_student":pass_count}
    
    
def get_sem_performance_analysis(sem):
    if Performance.objects.filter(sem=sem, regulation=sem.regulation,batch=sem.batch).exists():
        pers = Performance.objects.all().filter(sem=sem, regulation=sem.regulation,batch=sem.batch)
        fail_count = 0
        pass_count = 0
        register_count = 0
        cgpa = []
        no_of_back = []
        
        for per in pers:
            if per.pass_or_fail == False:
                fail_count +=1
                no_of_back.append(per.no_of_backlog)
            else:
                pass_count +=1
            register_count +=1
            cgpa.append(per.SCGPA)
            
        cgpa_analysis = {}
        back_data = {}
        for i in range(len(cgpa)):
            if cgpa[i] in cgpa_analysis:
                cgpa_analysis[cgpa[i]] +=1
            else:
                cgpa_analysis[cgpa[i]] = 1
                
        for i in range(len(no_of_back)):
            if no_of_back[i] in back_data:
                back_data[no_of_back[i]] += 1
            else:
                back_data[no_of_back[i]] = 1
        data = {}
        data["CGPA"] = cgpa_analysis
        data["Fail_count"] = fail_count
        data["Pass_count"] = pass_count
        data["Total_Registered"] = register_count
        data["Back_data"] = back_data
    
        return data

    return 0
            
            
        
        
        
        
        
def get_subject_analysis_data(sem):
    if Semester.objects.filter(id=sem.id).exists():
        sem = Semester.objects.get(id=sem.id)
        batch = sem.batch
        reg = sem.regulation
        branch = sem.branch
        
        subjs = Subjects.objects.all().filter(sem=sem,batch=batch,regulation=reg,branch=branch)
        subj_list = sem.subject.split(',')
        title_code = title_and_code(subj_list)
        code = title_code[0]
        title = title_code[1]
        data = {}
        sem_data = {}
        for i in range(len(code)):
            d = subj_analysis_one_more(sem,batch,reg,branch,code[i],title[i])
            data[code[i]] = {title[i]:d}
        sem_data["Subjects"] = data
        per = get_sem_performance_analysis(sem)
        sem_data["Semester PerFormance"] = per
    return sem_data











