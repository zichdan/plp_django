from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def about_us(request):
    return render (request, 'about.html', {})

def articles(request):
    posts = [
        {
            'author': '"Ann"',
            'tittle': 'Blog post 1',
            'content': 'First post content',
            'date': 'August 10, 2020'
        },
        {
            'author': "'Jane'",
            'tittle': 'Blog post 2',
            'content': 'Second post content',
            'date': 'August 1, 2020'
        }
    ]
    # blog = get_object_or_404(Post)
    
    blog = Post.objects.all()
    
    return render (request, 'post.html', {"articles": posts, "blogs": blog})

