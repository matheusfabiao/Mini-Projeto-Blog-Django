from django.shortcuts import render
from .models import Post

def blog_home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def index(request):
    latest_posts = Post.objects.all().order_by('-created_at')[:3]  # Exibe os 3 posts mais recentes
    return render(request, 'blog/index.html', {'latest_posts': latest_posts})