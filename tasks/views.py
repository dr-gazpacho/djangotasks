from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User, Task

def index(request):
    tasks = Task.objects.all()
    context = {
        "tasks_total": tasks
    }
    return render(request, "tasks/index.html", context)

def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('tasks:tasks_list')

def api(request):
    print(request)
    # Return JsonResponse instead of a string
    return JsonResponse({
        "message": "API is working",
        "status": "success"
    })
