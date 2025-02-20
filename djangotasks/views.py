from django.shortcuts import render

def index(request):
    body = "this is the body of the application"
    context = {
        "application_index": body
    }
    return render(request, "djangotasks/index.html", context)
