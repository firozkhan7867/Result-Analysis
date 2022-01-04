from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('upload',views.upload,name="upload"),
    path('data',views.data,name="upload_data"),
    path('backlog',views.backlogupload,name="backlog"),
    path('backdata',views.backlogdata,name="backlog_data"),
    path('subj/<int:sem_id>',views.get_sem_analysis,name="sem_data"),
    path('student',views.student_detail,name="student"),
    path('student/<int:sem_id>',views.get_sect_analysis,name="student_data")
]