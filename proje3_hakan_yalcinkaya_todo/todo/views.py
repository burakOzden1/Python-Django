from django.shortcuts import render
from .models import Todo
# from django.http import HttpResponse
from django.http import Http404


def home_view(request):
    # todos = Todo.objects.all()
    # todolarimizin hepsini anasayfa uzerinde gosterebilmek icin bu ifadeyi kullandik. todo_list.html icerisinden cagirdik.

    # todosActive = Todo.objects.filter(is_active=True) # Bunlar denemeydi
    # todosPassive = Todo.objects.filter(is_active=False) # Bunlar denemeydi

    todos = Todo.objects.filter(
        is_active = True,
        # title__icontains = "todo",
    ) # Bunlar denemeydi
    
    context = dict(
        todos=todos,
        # todosActive=todosActive, # Bunlar denemeydi
        # todosPassive=todosPassive, # Bunlar denemeydi
    )
    return render(request, 'todo/todo_list.html', context) # config/urls.py


def todo_detail_view(request, id):
    try:
        todo = Todo.objects.get(pk=id)
        context = dict(
            todo=todo,
        )
        return render(request, 'todo/todo_detail.html', context)
    except Todo.DoesNotExist:
        raise Http404