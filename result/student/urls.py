from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('upload',views.upload,name="upload"),
    path('data',views.data,name="upload_data"),
    path('backlog',views.backlogupload,name="backlog"),
    path('backdata',views.backlogdata,name="backlog_data"),
]
