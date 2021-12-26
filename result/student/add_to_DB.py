from pandas.core.indexing import convert_to_index_sliceable
from student.preprocesssing import get_subj_list, get_transformed_data
from .models import BacklogSubject, Batch, Performance, Semester, Subjects,Student,Regulation, Branch
from .back_log_handler import add_backlog
import pandas as pd

def extract_name(subj_name):
    names = subj_name.split("-")
    if len(names) > 1:
        code = names[0].strip()
        name = names[1].strip()
        return [code,name]
    else:
        return names
    
def add_student(sem,roll):
    batch = Batch.objects.get(id=sem.batch.id)
    for i in range(len(roll)):
        if Student.objects.filter(roll=roll[i]).exists():
            student = Student.objects.get(roll=roll[i])
            if sem not in student.sem.all():
                student.sem.add(sem)
                student.save() 
        else:
            student = Student(roll=roll[i], regulation= sem.regulation, branch=sem.branch,batch=batch)
            student.save()
            student.sem.add(sem)
            student.save()
    pass



def add_subject(data,subj_name,code,sem,roll):
    credit = list(map(float,data["Credit"]))
    batch = Batch.objects.get(id=sem.batch.id)
    # print(type(credit[1]))
    # print(credit[1])
    # print(type(credit))
    cgpa = list(map(float,data["CGPA"]))
    for i in range(len(data)):
        attendance_data = data["Attendance"]
        result_data = data["Result"]
        credit_data = credit[i]
        grade_data = data["Grade"]
        cgpa_data = cgpa[i]
        student_roll = Student.objects.get(roll=roll[i])
        
        if Subjects.objects.filter(code=code,roll=student_roll).exists():
            pass
        else:
            subj = Subjects(roll=student_roll,name=subj_name,code=code,branch=sem.branch, regulation=sem.regulation,
                            sem=sem,credit=credit_data,result=result_data[i],attendance=attendance_data[i],
                            batch=batch,grade=grade_data[i],cgpa=cgpa_data)
            subj.save()
            
            subj = Subjects.objects.get(id=subj.id)
            if subj.result == "F":
                subj.fail = True
                subj.save()
                add_backlog(subj,student_roll)
            
        # print(f"{roll[i]} for {subj_name} having Attendance of {attendance_data[i]} and result is {result_data[i]} \n credit is {credit_data[i]} grade is {grade_data[i]} cgpa is {cgpa_data[i]}")
    
        
    
def add_performance_sem(data,roll,sem):
    data["Registered"] = list(map(int,data["Registered"]))
    data["Pass"] = list(map(int,data["Pass"]))
    data["TCR"] = list(map(float,data["TCR"]))
    data["TCP"] = list(map(float,data["TCP"]))
    data["SCGPA"] = list(map(float,data["SCGPA"]))
    
    batch = Batch.objects.get(id=sem.batch.id)
    
    for i in range(len(data)):
        registered_data = data["Registered"]
        no_of_pass_data = data["Pass"]
        TCR_data = data["TCR"]
        TCP_data = data["TCP"]
        scgpa = data["SCGPA"]
        student_roll = Student.objects.get(roll=roll[i])
        no_of_backlog = registered_data[i] - no_of_pass_data[i]
        if no_of_backlog < 1:
            pass_or_fail = True
        else:
            pass_or_fail = False
        perform = Performance(roll=student_roll, regulation=sem.regulation,sem=sem,
                              registered=registered_data[i], no_of_pass=no_of_pass_data[i], 
                              no_of_backlog=no_of_backlog, pass_or_fail=pass_or_fail,
                              TCR=TCR_data[i], TCP=TCP_data[i], SCGPA=scgpa[i], batch=batch)
        perform.save()
        
        get_perform = Performance.objects.get(id=perform.id)
        
        subjs = Subjects.objects.all().filter(sem=sem,roll=student_roll)
        for j in subjs:
            sub = Subjects.objects.get(id=j.id)
            get_perform.subject.add(sub)
            get_perform.save()
        

    
    
def split_data(data,sem_id):
    sem = Semester.objects.get(id=sem_id)
    data = pd.read_excel(data)
    title = get_subj_list(data,6)
    di = get_transformed_data(data)
    
    
    # compulsory add this line to add new students in the database
    add_student(sem,di[1])
    # d1 = di[0][title[-1]]
    for i in di[0].keys():
        code_and_subj = extract_name(i)
        if len(code_and_subj) > 1:
            subj_name = code_and_subj[1]
            code = code_and_subj[0]
            data = di[0][i]
            add_subject(data,subj_name,code,sem,di[1])
            
        else:
            add_performance_sem(di[0][i],di[1],sem)

        
            
            
    
    
    