from django.shortcuts import render
from .models import Post


def render_all_posts(request):
    all_posts = Post.objects.all()
    return render(request=request, template_name='post/all_posts.html', context = {"all_posts": all_posts})