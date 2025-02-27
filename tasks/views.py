from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    tasks_body= "this is the body of the tasks"
    context = {
        "tasks_index": tasks_body
    }
    return render(request, "tasks/index.html", context)

def api(request):
    print(request)
    # Return JsonResponse instead of a string
    return JsonResponse({
        "message": "API is working",
        "status": "success"
    })
