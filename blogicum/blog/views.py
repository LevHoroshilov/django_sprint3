import datetime

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.order_by('pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        pub_date__lte=datetime.datetime.now(),
        is_published=True,
        category__is_published=True,
        id=id)
    context = {'post': post}
    template = 'blog/detail.html'
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    post_list = Post.objects.filter(
        category__slug=category_slug,
    )
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)
