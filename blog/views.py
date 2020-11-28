from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from django_currentuser.middleware import get_current_authenticated_user


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_public=True).order_by('-date_posted')
    template_name = 'blog/index.html'
    context_object_name = "posts"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'is_public']
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'is_public']
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def detail_view(request, pk):
    author = get_current_authenticated_user()
    posts = Post.objects.get(pk=pk)
    context = {
        'author': author,
        'object': posts,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def all_my_posts(request):
    posts = Post.objects.filter(author=get_current_authenticated_user()).order_by('-date_posted')
    context = {
        "posts": posts,
    }

    return render(request, 'blog/all_user_posts.html', context)
