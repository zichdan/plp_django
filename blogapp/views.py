from django.shortcuts import render,redirect
from django.urls import reverse

from .models import Post
from blogapp.forms import PostForm

from django.shortcuts import get_object_or_404






# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def about_us(request):
    return render (request, 'about.html', {})

def articles(request):
    posts = Post.objects.all()
    
    context = {
        'posts': posts
    }
    
    return render (request, 'post.html', context)

def articles_details(request, pk):
    # Post = Post.objects.get(pk=pk) # slect * from where id = pk
                    # OR
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'post_details.html', context)

    
def articles_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('articles'))
    else:
        form = PostForm()
    
    context = {
        "form" : form
    }
    return render(request, "create.html", context)


def article_update(request, pk):
    post_obj = Post.objects.get(pk=pk)
    
    if request.method=="POST":
        form = PostForm(instance=post_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("details", args=(pk,)))
    else:
        form = PostForm(instance=post_obj)
    context = {
        "form" : form,
        "object": post_obj
    }    
    return render(request, 'create.html', context)
    
def article_delete(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)
    post_obj.delete()
    
    return redirect(reverse("articles"))
    
    

    
    
    
    
# def article_delete(request, pk):
#     product_obj = get_object_or_404(Product, pk=pk)
#     product_obj.delete()
#     return redirect(reverse("crudapp:product_list"))    
    

     
        
            
        
    
    
    
    
    
    
    
    
    
    