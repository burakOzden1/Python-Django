from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def home(request):
    context = {"platform": f"Django Platformu Kullanildi ve randint ile donen veri {randint(1, 100)}"}
    return render(request, 'page/home_page.html', context)