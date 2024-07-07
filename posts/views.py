from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts
from .forms import PostForm


def get_all(request):
    posts = Posts.objects.all()

    context = {
        'posts': posts,
        'page_title': 'List of Notes'
    }

    return render(request, 'posts/index.html', context)


def get_one(request, pk):
    post = get_object_or_404(Posts, pk=pk)

    return render(request, 'posts/details.html', {'post': post})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts')
    else:
        form = PostForm()

    return render(request, 'posts/form.html', {'form': form})


def update(request, pk):
    post = get_object_or_404(Posts, pk=pk)

    if (request.method == 'POST'):
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/form.html', {'form': form})


def delete(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    post.delete()
    return redirect('posts')
