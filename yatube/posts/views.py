from django.shortcuts import get_object_or_404, render
from .models import Group, Post

IN_PAGE = 10


def index(request):
    """ 10 post entries """

    posts = Post.objects.all()[:IN_PAGE]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """ 10 group entries """

    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:IN_PAGE]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
