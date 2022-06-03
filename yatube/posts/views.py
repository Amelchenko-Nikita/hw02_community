from django.shortcuts import render, get_object_or_404
from .models import Post, Group, Meta

# Create your views here


def index(request):
    date = Meta.ordering
    posts = Post.objects.order_by(date)[:10]
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    date = Meta.ordering
    posts = Post.objects.filter(group=group).order_by(date)[:10]
    group = get_object_or_404(Group, slug=slug)
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
