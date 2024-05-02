from django.shortcuts import render
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, "todo/index.html", {"todos": todos})
