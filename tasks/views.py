from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Task

def index(request):
    print(request.user)
    tasks = Task.objects.all()
    context = {
        "tasks_total": tasks
    }
    return render(request, "tasks/index.html", context)

def api(request):
    print(request)
    # Return JsonResponse instead of a string
    return JsonResponse({
        "message": "API is working",
        "status": "success"
    })
