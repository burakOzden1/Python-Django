from django.shortcuts import render
from .forms import BlogPostModelForm
from .models import Category, Tag, BlogPost


def create_blog_post_view(request):
    form = BlogPostModelForm()
    context = dict(form=form)
    if request.method == 'POST':
        pass
        # print(request.POST) # forma girdigimiz bilgileri terminal uzerinde gorduk.
    return render(request, "blog/create_blog_post.html", context)
