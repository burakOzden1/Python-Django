from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def home_view(request):
    # todos = Todo.objects.all()
    # todos = Todo.objects.filter(is_active=True)
    # todos = todos.filter(title__icontains="todo")

    todos = Todo.objects.filter(
        is_active = True,
        # title__icontains="todo",
    )
    context = dict(
        todos = todos
    )
    return render(request, 'todo/todo_list.html', context)