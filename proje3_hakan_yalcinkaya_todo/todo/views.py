from django.shortcuts import render
from .models import Todo

# from django.http import HttpResponse
from django.http import Http404


def home_view(request):
    # todos = Todo.objects.all()
    # todolarimizin hepsini anasayfa uzerinde gosterebilmek icin bu ifadeyi kullandik. todo_list.html icerisinden cagirdik.

    # todosActive = Todo.objects.filter(is_active=True) # Bunlar denemeydi
    # todosPassive = Todo.objects.filter(is_active=False) # Bunlar denemeydi

<<<<<<< HEAD
    # todos = Todo.objects.filter(
    #     is_active = True,
    #     # title__icontains = "todo",
    # ) # Bunlar denemeydi

=======
    todos = Todo.objects.filter(
        is_active = True,
        # title__icontains = "todo",
    ) # Bunlar denemeydi
    
>>>>>>> 11c91e0803c6d876662437be42bc50c66036dcb1
    context = dict(
        todos=todos,
        # todosActive=todosActive, # Bunlar denemeydi
        # todosPassive=todosPassive, # Bunlar denemeydi
    )
<<<<<<< HEAD
    return render(request, "todo/todo_list.html", context)  # config/urls.py
=======
    return render(request, 'todo/todo_list.html', context) # config/urls.py
>>>>>>> 11c91e0803c6d876662437be42bc50c66036dcb1


def todo_detail_view(request, id):
    try:
        todo = Todo.objects.get(pk=id)
        context = dict(
            todo=todo,
        )
<<<<<<< HEAD
        return render(request, "todo/todo_detail.html", context)
    except Todo.DoesNotExist:
        raise Http404
=======
        return render(request, 'todo/todo_detail.html', context)
    except Todo.DoesNotExist:
        raise Http404
>>>>>>> 11c91e0803c6d876662437be42bc50c66036dcb1
