from django.shortcuts import render,get_object_or_404
from blog.models import Post

import datetime
def index(request):
    template = 'blog/index.html'
    posts = Post.objects.filter(is_published=True,category__is_published=True).order_by('pub_date')
    context = {'posts': posts}
    return render(request, template, context)


def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.filter(),
        pk=pk
    )
    context = {'post': post}
    template = 'blog/detail.html'
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'slug': category_slug}
    return render(request, template, context)
