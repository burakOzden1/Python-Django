from django.shortcuts import render, redirect, get_object_or_404
from user_profile.models import Profile
from blog.models import BlogPost



def all_posts_view(request, user_slug):
    profile = get_object_or_404(Profile, slug=user_slug)
    context = dict(
        profile=profile,
        posts = BlogPost.objects.filter(user=profile.user, is_active=True),
    )
    return render(request, 'read/all_posts.html', context)