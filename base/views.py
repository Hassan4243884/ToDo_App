from django.shortcuts import render,redirect
from .models import Tag,Task
from .forms import TaskForm
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def index(request):
    tasks = Task.objects.filter(completed=False)[:2]
    tags = Tag.objects.all()
    template_name = "base/index.html"
    context = {"tasks":tasks,"tags":tags,}
    return render(request,template_name,context)

def dashboard(request):
    text = "Pending"
    q = request.GET.get("q") if request.GET.get("q") is not None else "" 
    tasks = Task.objects.filter(Q(tag__slug__icontains = q) &  Q(completed=False) )
    total = tasks.count()
    template_name = "base/dashboard.html"
    context = {"tasks":tasks,"total":total,"text":text}
    return render(request,template_name,context)


def createTask(request):
    path = reverse("add")
    form = TaskForm
    template_name = "base/form.html"
    context = {"form":form,"path":path}
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")
    return render(request,template_name,context)

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    path = task.get_update_url()
    form = TaskForm(instance=task)
    template_name = "base/form.html"
    context = {"form":form,"path":path}

    if request.method == "POST":
        new_form = TaskForm(request.POST,instance=task)
        if new_form.is_valid:
            # print(v"{new_form.id}")
            new_form.save()
            return redirect("dash")

    return render(request,template_name,context)

def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    template_name = "base/delete.html"
    if request.method == "POST":
        task.delete()
        return redirect("home")
    return render(request,template_name,{"task":task,})

def profile(request):
    total = Task.objects.all().count()
    completed = Task.objects.filter(completed=True).count()
    rate = (int(total)*int(completed))/10
    template_name = "base/profile.html"
    return render(request,template_name,{"total":total,"completed":completed,"rate":rate})

def completedTasks(request):
    text = "Completed"
    tasks = Task.objects.filter(completed = True)
    total = tasks.count()
    template_name = "base/dashboard.html"
    context = {"tasks":tasks,"total":total,"text":text}
    return render(request,template_name,context)

def complete(request,pk):
    task = Task.objects.get(id=pk)
    task.completed = True
    task.save()
    return redirect("dash-completed")