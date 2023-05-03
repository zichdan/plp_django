from django.shortcuts import render

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
    
    return render (request, 'post.html', {"articles": posts})

