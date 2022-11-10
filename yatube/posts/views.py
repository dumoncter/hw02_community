from django.shortcuts import get_object_or_404, render
from .models import Group, Post

POSTS_ON_PAGE = 10


def index(request):
    """ 10 post entries """

    posts = Post.objects.all()[:POSTS_ON_PAGE]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """ 10 group entries """

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_ON_PAGE]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
