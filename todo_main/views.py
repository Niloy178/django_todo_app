from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task 


def home(req):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {
        'tasks': tasks,
        'completed': completed,
    }
    return render(req, 'home.html', context)