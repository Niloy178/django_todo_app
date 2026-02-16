from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from .models import Task
# Create your views here.

# Add Task
def addTask(req):
    print(req.POST['task'])
    Task.objects.create(task=req.POST['task'])
    return redirect('home')

# Mark a task as done
def mark_done(req, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

# Mark a task as Undone
def mark_undone(req, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed=False
    task.save()
    return redirect("home")
# Delete a task
def delete(req, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("home")

# Edit Task
def edit_task(req, pk):
    task=get_object_or_404(Task, pk=pk)
    if req.method == "POST":
        task=get_object_or_404(Task, pk=pk)
        task.task=req.POST["task"]
        task.save()
        return redirect("home")
    else:
        context={
        "task": task,
        }
        return render(req, "edit_task.html", context)