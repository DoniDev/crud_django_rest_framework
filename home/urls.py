from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name='home'),
    path('task/list',views.tasklist,name='list'),
    path('task/detail/<str:pk>/',views.taskdetail,name='task-detail'),
    path('task/create/',views.taskcreate,name='task-create'),
    path('task/update/<str:pk>',views.taskupdate,name='task-update'),
    path('task/delete/<str:pk>',views.taskdelete,name='task-delete'),


]