import pandas as pd

from student.models import Student, Subjects
pd.options.mode.chained_assignment = None
def get_subj_list(data,row_index):
    title = data.iloc[row_index]
    title = title.dropna()[2:]
    return list(title)

def get_transformed_data(data):
    num_of_subj = get_subj_list(data,6)
    count = len(num_of_subj)
    data = data.iloc[11:,1:]
    data = data.dropna()
    subj_dict = {}
    for i in range(1,count+1):
        subj_dict[num_of_subj[i-1]] = ""
    roll = data.iloc[:,0]
    roll = roll.reset_index(drop=True)
    data = data.iloc[:,1:]
    data = data.reset_index(drop=True)
    for i in range(count):
        if count - i == 1:
            subj_data = data.iloc[:,i*5:(i*5)+5]
            subj_data.rename(columns={f"Unnamed: {(i*5)+2}":"Registered",f"Unnamed: {(i*5)+3}":"Pass",f"Unnamed: {(i*5)+4}":"TCR",f"Unnamed: {(i*5)+5}":"TCP",f"Unnamed: {(i*5)+6}":"SCGPA"},inplace=True)
            subj_data["Roll"] = roll
        else:
            subj_data = data.iloc[:,i*5:(i*5)+5]
            subj_data.rename(columns={f"Unnamed: {(i*5)+2}":"Attendance",f"Unnamed: {(i*5)+3}":"Result",f"Unnamed: {(i*5)+4}":"Credit",f"Unnamed: {(i*5)+5}":"Grade",f"Unnamed: {(i*5)+6}":"CGPA"},inplace=True)
            subj_data["Roll"] = roll
        subj_dict[list(subj_dict.keys())[i]] = subj_data
    return [subj_dict,roll]


def describe_about_column(data):
    data = pd.Series(data)
    data_describe = dict(data.value_counts())
    return data_describe

def get_subject_analysis(sem,subj):
    subject_data = Subjects.objects.all().filter(name=subj)
    attnd = [data.cgpa for data in subject_data]
    attnd_value_count = describe_about_column(attnd)
    result = [data.result for data in subject_data]
    result_value_count = describe_about_column(result)
    num_of_failes = result_value_count['F']
    grade = [data.grade for data in subject_data]
    grade_value_count = describe_about_column(
        grade)
    
    




def get_section_list(students):
    sect = {}
    for stu in students:
        if stu.section not in sect:
            sect[stu.section] = 1
        else:
            sect[stu.section] +=1
    
    return sect





