from django.shortcuts import render
from .models import Todo
# from django.http import HttpResponse


def home_view(request):
    todos = Todo.objects.all()
    # todolarimizin hepsini anasayfa uzerinde gosterebilmek icin bu ifadeyi kullandik. todo_list.html icerisinden cagirdik.

    # todosActive = Todo.objects.filter(is_active=True) # Bunlar denemeydi
    # todosPassive = Todo.objects.filter(is_active=False) # Bunlar denemeydi

    # todo = Todo.objects.filter(
    #     is_active = True,
    #     title__icontains = "todo",
    # ) # Bunlar denemeydi
    
    context = dict(
        todos=todos,
        # todosActive=todosActive, # Bunlar denemeydi
        # todosPassive=todosPassive, # Bunlar denemeydi
    )
    return render(request, 'todo/todo_list.html', context) # config/urls.py