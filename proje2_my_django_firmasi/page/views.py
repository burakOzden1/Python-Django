from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def home_view(request):
    page_title = "Django"
    context = dict(
        page_title=page_title,
    )
    return render(request, 'page/home_page.html', context)

def about_us_view(request):
    page_title = "Hakkımızda"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate imperdiet ligula, ac ullamcorper nibh finibus et. Nulla lacus elit, mattis vitae sapien nec, accumsan convallis felis. Sed iaculis justo congue est accumsan pretium. Etiam eget laoreet libero, nec euismod ex. Etiam a tellus et ligula lobortis condimentum et nec dolor. Cras sit amet magna magna. Sed sit amet imperdiet tellus, at dignissim velit. Vivamus consectetur mauris orci, vel feugiat arcu maximus at. Morbi quis malesuada justo, sit amet malesuada eros. Quisque pellentesque vulputate suscipit."
    context = dict(
         page_title = page_title,
         hero_content = hero_content,
    )
    return render(request, 'page/about_us.html', context)

def vision_view(request):
    page_title = "Vizyonumuz"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate imperdiet ligula, ac ullamcorper nibh finibus et. Nulla lacus elit, mattis vitae sapien nec, accumsan convallis felis. Sed iaculis justo congue est accumsan pretium. Etiam eget laoreet libero, nec euismod ex. Etiam a tellus et ligula lobortis condimentum et nec dolor. Cras sit amet magna magna. Sed sit amet imperdiet tellus, at dignissim velit. Vivamus consectetur mauris orci, vel feugiat arcu maximus at. Morbi quis malesuada justo, sit amet malesuada eros. Quisque pellentesque vulputate suscipit."
    context = dict(
         page_title = page_title,
         hero_content = hero_content,
    )
    return render(request, 'page/vision.html', context)

def contact_us_view(request):
    page_title = "İletişim"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate imperdiet ligula, ac ullamcorper nibh finibus et. Nulla lacus elit, mattis vitae sapien nec, accumsan convallis felis. Sed iaculis justo congue est accumsan pretium. Etiam eget laoreet libero, nec euismod ex. Etiam a tellus et ligula lobortis condimentum et nec dolor. Cras sit amet magna magna. Sed sit amet imperdiet tellus, at dignissim velit. Vivamus consectetur mauris orci, vel feugiat arcu maximus at. Morbi quis malesuada justo, sit amet malesuada eros. Quisque pellentesque vulputate suscipit."
    context = dict(
         page_title = page_title,
         hero_content = hero_content,
    )
    return render(request, 'page/contact_us.html', context)