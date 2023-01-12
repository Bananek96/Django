from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Answer
from django.utils import timezone
from .forms import PostForm, AnswerForm
from django.core.paginator import Paginator


def posts_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 5)
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
            post.author.id = request.user.id
            post.published_date = timezone.now()
            post.save()
            return redirect('forum:post', pk=post.pk)
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
            return redirect('forum:post', pk=post.pk)
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
            answer.author.id = request.user.id
            answer.post = post
            answer.save()
            return redirect('forum:answer', pk=post.pk, an=answer.pk)
    else:
        form = AnswerForm()
    return render(request, 'forum/comments.html', {'form': form})


def answer_detail(request, pk, an):
    post = get_object_or_404(Post, pk=pk)
    answer = get_object_or_404(Answer, pk=an)
    return render(request, 'forum/view_answer.html', {'post': post}, {'answer': answer})

def answer_edit(request, pk, an):
    post = get_object_or_404(Post, pk=pk)
    answer = get_object_or_404(Answer, an=an)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.post = post
            answer.save()
            return redirect('forum:answer', pk=post.pk, an=answer.pk)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'forum/comments.html', {'form': form})


def delete_answer(request, pk, an):
    answer = get_object_or_404(Answer, pk=an)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.post = post
            answer.delete()
            return redirect('forum:post')
        else:
            form = AnswerForm(instance=answer)
    return render(request, 'forum/answer_confirm_delete.html', {'form': form})
