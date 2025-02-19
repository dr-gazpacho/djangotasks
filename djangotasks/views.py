from django.shortcuts import render

def index(request):
    hello_world = "Hello world"
    context = {
        "hello_world": hello_world
    }
    return render(request, "djangotasks/index.html", context)
