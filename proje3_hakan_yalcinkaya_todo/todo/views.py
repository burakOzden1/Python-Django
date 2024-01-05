from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    context = dict()
    return render(request, 'todo/todo_list.html', context) # config/urls.py