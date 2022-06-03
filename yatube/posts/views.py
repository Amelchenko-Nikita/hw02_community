from django.shortcuts import render, get_object_or_404 
from .models import Post, Group 

 

# Create your views here 


def index(request): 
    posts = Post.objects.order_by('-pub_date')[:10] 
    template = 'posts/index.html' 
    context = { 
        'text': 'Последние обновления на сайте', 
        'posts': posts, 
    } 
    return render(request, template, context)


def group_posts(request, slug): 
    group = get_object_or_404(Group, slug=slug) 
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10] 
    template = 'posts/group_list.html' 
    context = { 

        'group': group, 
        'posts': posts, 
        'text': "Здесь будет информация о группах проекта Yatube", 
    } 

    return render(request, template, context)
