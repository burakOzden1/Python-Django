from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse
# from django.http import Http404

# My Models:

from .models import Todo, Category


@login_required(login_url="/admin/login/")
def home_view(request):
    # todos = Todo.objects.all()
    # todolarimizin hepsini anasayfa uzerinde gosterebilmek icin bu ifadeyi kullandik. todo_list.html icerisinden cagirdik.

    # todosActive = Todo.objects.filter(is_active=True) # Bunlar denemeydi
    # todosPassive = Todo.objects.filter(is_active=False) # Bunlar denemeydi

    todos = Todo.objects.filter(
        user=request.user,  # istegi gonderen kullaniciyi al dedik.
        is_active=True,
        # title__icontains = "todo",
    )  # Bunlar denemeydi

    context = dict(
        todos=todos,
        # todosActive=todosActive, # Bunlar denemeydi
        # todosPassive=todosPassive, # Bunlar denemeydi
    )
    return render(request, "todo/todo_list.html", context)  # config/urls.py


# def todo_detail_view(request, id):
#     try:
#         todo = Todo.objects.get(pk=id)
#         context = dict(
#             todo=todo,
#         )
#         return render(request, "todo/todo_detail.html", context)
#     except Todo.DoesNotExist:
#         raise Http404


@login_required(login_url="/admin/login/")
def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    todos = Todo.objects.filter(
        is_active=True,
        category=category,
        user=request.user,
    )  # aktif olan ve category bilgisi olan todolari al ve getir.
    context = dict(
        todos=todos,
        category=category,
    )
    return render(request, "todo/todo_list.html", context)


@login_required(login_url="/admin/login/")
def todo_detail_view(request, category_slug, id):
    todo = get_object_or_404(
        Todo, category__slug=category_slug, pk=id, user=request.user
    )
    context = dict(
        todo=todo,
    )
    return render(request, "todo/todo_detail.html", context)
