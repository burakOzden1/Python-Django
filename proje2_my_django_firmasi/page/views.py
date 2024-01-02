from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Ana Sayfaya Hoşgeldiniz..')

def urunler(request):
    return HttpResponse('Ürünler Sayfasına Hoşgeldiniz..')

def hakkimizda(request):
    return HttpResponse('Hakkımızda Sayfasına Hoşgeldiniz..')

def iletisim(request):
    return HttpResponse('İletişim Sayfasına Hoşgeldiniz..')