from django.shortcuts import render
from django.http import HttpResponse
from random import randint

FAKE_DB_PROJECTS = [
    f"https://picsum.photos/id/{id}/100/80" for id in range(21, 29)
]

FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/400" for id in range(24, 28)
]

def home_view(request):
    context = dict(
        FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
        FAKE_DB_CAROUSEL=FAKE_DB_CAROUSEL,
    )
    return render(request, 'page/home_page.html', context)

def about_us_view(request):
    page_title = "Hakkımızda"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate imperdiet ligula, ac ullamcorper nibh finibus et. Nulla lacus elit, mattis vitae sapien nec, accumsan convallis felis. Sed iaculis justo congue est accumsan pretium. Etiam eget laoreet libero, nec euismod ex. Etiam a tellus et ligula lobortis condimentum et nec dolor. Cras sit amet magna magna. Sed sit amet imperdiet tellus, at dignissim velit. Vivamus consectetur mauris orci, vel feugiat arcu maximus at. Morbi quis malesuada justo, sit amet malesuada eros. Quisque pellentesque vulputate suscipit."
    context = dict(
         page_title = page_title,
         hero_content = hero_content,
         FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
    )
    return render(request, 'page/about_us.html', context)

def vision_view(request):
    page_title = "Vizyonumuz"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate imperdiet ligula, ac ullamcorper nibh finibus et. Nulla lacus elit, mattis vitae sapien nec, accumsan convallis felis. Sed iaculis justo congue est accumsan pretium. Etiam eget laoreet libero, nec euismod ex. Etiam a tellus et ligula lobortis condimentum et nec dolor. Cras sit amet magna magna. Sed sit amet imperdiet tellus, at dignissim velit. Vivamus consectetur mauris orci, vel feugiat arcu maximus at. Morbi quis malesuada justo, sit amet malesuada eros. Quisque pellentesque vulputate suscipit."
    context = dict(
         page_title = page_title,
         hero_content = hero_content,
         FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
    )
    return render(request, 'page/vision.html', context)

def contact_us_view(request):
    page_title = "İletişim"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vulputate imperdiet ligula, ac ullamcorper nibh finibus et. Nulla lacus elit, mattis vitae sapien nec, accumsan convallis felis. Sed iaculis justo congue est accumsan pretium. Etiam eget laoreet libero, nec euismod ex. Etiam a tellus et ligula lobortis condimentum et nec dolor. Cras sit amet magna magna. Sed sit amet imperdiet tellus, at dignissim velit. Vivamus consectetur mauris orci, vel feugiat arcu maximus at. Morbi quis malesuada justo, sit amet malesuada eros. Quisque pellentesque vulputate suscipit."
    context = dict(
        page_title = page_title,
        hero_content = hero_content,
        FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
    )
    return render(request, 'page/contact_us.html', context)