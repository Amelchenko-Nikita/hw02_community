from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Post, Group, Meta

# Create your views here

def index(request):
    date = Meta.ordering
    posts = Post.objects.order_by(date)
    context = {
        'POSTS_PER_PAGE': settings.POSTS_PER_PAGE,
        'posts':posts
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    context = {
        'group':group,
        'posts':posts,
    }
    return render(request, template, context)
