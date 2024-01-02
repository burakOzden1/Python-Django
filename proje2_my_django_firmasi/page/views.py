from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def home_view(request):
    context = {}
    return render(request, 'page/home_page.html', context)

def about_us_view(request):
    page_title = "Hakkımızda | "
    context = dict(
         page_title = page_title,
    )
    return render(request, 'page/about_us.html', context)

def vision_view(request):
    page_title = "Vizyonumuz | "
    context = dict(
         page_title = page_title,
    )
    return render(request, 'page/vision.html', context)

def contact_us_view(request):
    page_title = "İletişim | "
    context = dict(
         page_title = page_title,
    )
    return render(request, 'page/contact_us.html', context)