from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task 


def home(req):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks': tasks,
    }
    return render(req, 'home.html', context)