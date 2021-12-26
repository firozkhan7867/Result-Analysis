import pandas as pd
from student.models import Attempt, BacklogSubject, Batch, Semester, Student, Subjects, Performance
from student.preprocesssing import get_subj_list, get_transformed_data


def add_backlog(subj,student_roll):
    subj = Subjects.objects.get(id=subj.id)
    batch = Batch.objects.get(id=subj.batch.id)
    sem = subj.sem
    reg = subj.regulation
    branch = subj.branch
    code = subj.code
    subj_name = subj
    if subj.roll.roll == student_roll.roll:
        backlog = BacklogSubject(roll=student_roll,sem=sem,reg=reg,branch=branch,subj_code=code,subject=subj_name,count=1,
                                 batch=batch)
        backlog.save()

def update_performance(subj):
    perf = Performance.objects.get(sem=subj.sem,roll=subj.roll)
    perf.no_of_pass += 1
    perf.no_of_backlog -=1
    perf.save()

def update_subject(attmpt):
    subj = Subjects.objects.get(id=attmpt.subj.id)
    subj.fail = False
    subj.credit = attmpt.credit
    subj.result = attmpt.result
    subj.attendance = attmpt.attendance
    subj.grade = attmpt.grade
    subj.cgpa = attmpt.cgpa
    subj.save()
    
    update_performance(subj)
        
def add_attempt_details(subject,sem,data,student_roll,attendance_data,batch,credit_data,result_data,grade_data,cgpa_data):
    
    sbj = Subjects.objects.get(id=subject.id)
    if sbj.fail == False:
        return None
    
    if result_data.lower() == "p":
        passed = True
    else:
        passed = False
        
    attmpt = Attempt(roll=student_roll,subj=subject,sem=sem,
                     batch=batch,credit=credit_data,result=result_data,
                     attendance=attendance_data,grade=grade_data,cgpa=cgpa_data,passed=passed)
    attmpt.save()
    attmpt.back_log.add(data)
    attmpt.save()
    
    backsubj = BacklogSubject.objects.get(id=data.id)
    backsubj.count += 1
    backsubj.passed = passed
    backsubj.save()
    
    if passed == True:
        update_subject(attmpt)
    
    
    
    
    
def add_attempt(data,subj_name,code,sem,roll):
    credit = list(map(float,data["Credit"]))
    batch = Batch.objects.get(id=sem.batch.id)
    cgpa = list(map(float,data["CGPA"]))
    
    
    for i in range(len(data)):
        attendance_data = data["Attendance"]
        result_data = data["Result"]
        credit_data = credit[i]
        grade_data = data["Grade"]
        cgpa_data = cgpa[i]
        student_roll = Student.objects.get(roll=roll[i])
        if BacklogSubject.objects.filter(roll=student_roll).exists():
            back_subj_data = BacklogSubject.objects.all().filter(roll=student_roll)
            if len(back_subj_data) > 1:
                for back_data in back_subj_data:
                    if back_data.subject.name == subj_name:
                        add_attempt_details(back_data.subject,back_data.sem,back_data,student_roll,attendance_data[i],batch,credit_data,result_data[i],grade_data[i],cgpa_data)
            else:
                back_data = back_subj_data[0]
                if back_data.subject.name == subj_name:
                    add_attempt_details(back_data.subject,back_data.sem,back_data,student_roll,attendance_data[i],batch,credit_data,result_data[i],grade_data[i],cgpa_data)
               

def extract_name(subj_name):
    names = subj_name.split("-")
    if len(names) > 1:
        code = names[0].strip()
        name = names[1].strip()
        return [code,name]
    else:
        return names

def split_data_backlog(data,sem_id):
    sem = Semester.objects.get(id=sem_id)
    data = pd.read_excel(data)
    title = get_subj_list(data,6)
    di = get_transformed_data(data)
    
    
    # compulsory add this line to add new students in the database
    # add_student(sem,di[1])
    # d1 = di[0][title[-1]]
    for i in di[0].keys():
        code_and_subj = extract_name(i)
        if len(code_and_subj) > 1:
            subj_name = code_and_subj[1]
            code = code_and_subj[0]
            data = di[0][i]
            add_attempt(data,subj_name,code,sem,di[1])
            
        # else:
        #     add_performance_sem(di[0][i],di[1],sem)
            

        
            
            
