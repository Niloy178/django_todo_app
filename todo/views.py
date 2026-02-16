from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Task
# Create your views here.

# Add Task
def addTask(req):
    print(req.POST['task'])
    Task.objects.create(task=req.POST['task'])
    return redirect('home')