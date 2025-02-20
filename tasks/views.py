from django.shortcuts import render

def index(request):
    tasks_body= "this is the body of the tasks"
    context = {
        "tasks_index": tasks_body
    }
    return render(request, "tasks/index.html", context)
