from django.shortcuts import redirect, render
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import CreatePost

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts': posts })

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', { 'post': post })

@login_required(login_url="users:login")
def post_new(request):
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:posts')
    else:
        form = CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form })

@login_required(login_url="users:login")
def post_edit(request, slug):
    post = Post.objects.get(slug=slug)

    if request.user != post.author:
        return redirect('posts:posts')
    
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:posts')
    else:
        form = CreatePost(instance=post)
    return render(request, 'posts/post_edit.html', { 'form': form})