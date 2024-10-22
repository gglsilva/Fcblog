from django.shortcuts import render
from .models import Post, Tag

# Create your views here.
def index(request):
    posts = Post.objects.prefetch_related('tags').all()
    context = {
        'posts': posts,
    }
    return render(request, 'core/index.html', context)