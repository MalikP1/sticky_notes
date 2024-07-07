from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts
from .forms import PostForm

'''
View to display a list of all posts.
Creates a context dictionary to pass data
and returns a rendered template with a list of the posts.
'''


def get_all(request):
    posts = Posts.objects.all()

    context = {
        'posts': posts,
        'page_title': 'List of Notes'
    }

    return render(request, 'posts/index.html', context)


'''
View to display details of a specific post.
Parameter pk is the primary key of the post,
returns the rendered template with details of the specified post.
'''


def get_one(request, pk):
    post = get_object_or_404(Posts, pk=pk)

    return render(request, 'posts/details.html', {'post': post})


'''
View to create a new post.
Returns rendered template for creating a new post.
'''


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


'''
View to update an existing post.
Returns rendered template for updating the specified post.
'''


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


'''
View to delete an existing post.
Returns a redirect to the list of posts after deletion.
'''


def delete(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    post.delete()
    return redirect('posts')
