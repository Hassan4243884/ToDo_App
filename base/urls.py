from venv import create
from django.urls import path
from .views import index,createTask,updateTask,dashboard,profile,deleteTask,completedTasks,complete
urlpatterns = [
    path("",index,name="home"),
    path("tasks/",dashboard,name="dash"),
    path("tasks/completed",completedTasks,name="dash-completed"),
    path("complete/<str:pk>/",complete,name="complete"),
    path("add/",createTask,name="add"),
    path("update/<str:pk>/",updateTask,name="update"),
    path("delete/<str:pk>/",deleteTask,name="delete"),
    path("profile/",profile,name="profile"),



]