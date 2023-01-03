from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm, AnswerForm
from django.core.paginator import Paginator


def posts_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'forum/index.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'forum/post.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('forum/post.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'forum/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('forum/index.html', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'forum/post_edit.html', {'form': form})


def add_answer(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.post = post
            answer.save()
            return redirect('forum/post.html', pk=post.pk)
    else:
        form = AnswerForm()
    return render(request, 'forum/comments.html', {'form': form})
