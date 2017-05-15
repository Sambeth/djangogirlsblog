from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {
        'posts': posts,
    }
    template = 'blog/post_list.html'
    return render(request, template, context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    template = 'blog/post_detail.html'
    return render(request, template, context)
