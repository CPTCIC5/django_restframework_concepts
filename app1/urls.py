from django.urls import path
from . import views

urlpatterns = [
    path('',views.test_prog,name='test_prog'),
    path('tasklist/',views.TaskList.as_view(),name='tasklist/'),
    path('taskdetail/<int:question_id>',views.taskdetail,name='taskdetail'),
    path('taskcreator/',views.TaskCreator.as_view(),name='taskcreator'),
    path('taskupdate/<int:question_id>/',views.taskupdate,name='taskupdate'),
    path('taskdelete/<int:question_id>/',views.taskdelete,name='taskdelete')
]
