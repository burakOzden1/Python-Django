from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BlogPostModelForm
from .models import Category, Tag, BlogPost


@login_required(login_url="user:login_view")
def create_blog_post_view(request):
    form = BlogPostModelForm()
    if request.method == "POST":
        # print(request.POST) # forma girdigimiz bilgileri terminal uzerinde gorduk.
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            print(form.cleaned_data)
            f.user = request.user
            # print(form.cleaned_data.get('tag'))
            # f.save()
    context = dict(form=form)
    return render(request, "blog/create_blog_post.html", context)
