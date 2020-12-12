from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from django_currentuser.middleware import get_current_authenticated_user, get_current_user
from django.core.paginator import Paginator


def get_user_settings_posts_per_page(user):
    """ Unauthenticated user has no attribute user_setting_pages """
    try:
        user_setting_pages = user.profile.blogposts_per_page
    except AttributeError:
        user_setting_pages = 4

    return user_setting_pages


class PostListView(ListView):
    def get_paginate_by(self, *args, **kwargs):
        user = get_current_authenticated_user()
        return get_user_settings_posts_per_page(user)

    model = Post
    queryset = Post.objects.filter(is_public=True).order_by('-date_posted')
    template_name = 'blog/blog_index.html'


class UserPostListView(ListView):
    def get_paginate_by(self, *args, **kwargs):
        user = get_current_authenticated_user()
        return get_user_settings_posts_per_page(user)

    model = Post
    template_name = 'blog/user_posts.html'

    def get_queryset(self):
        selected_author = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=selected_author, is_public=True).order_by('-date_posted')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'subtitle', 'content', 'is_public', 'tags']
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'content', 'is_public', 'tags']
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
def detail_view(request, slug):
    author = get_current_authenticated_user()
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        PostComment.objects.create(
            comment_author=request.user,
            to_post=post,
            comment_body=request.POST['comment']
        )
        messages.success(request, "You're comment was successfuly posted!")

        return redirect('post-detail', slug)
    comments = PostComment.objects.filter(to_post=post)
    context = {
        'author': author,
        'object': post,
        'comments': comments
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def all_my_posts(request):
    user_setting_pages = request.user.profile.tasks_per_page
    posts = Post.objects.filter(author=get_current_authenticated_user()).order_by('-date_posted')
    paginator = Paginator(posts, user_setting_pages)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": posts,
        "page_obj": page_obj,
    }

    return render(request, 'blog/all_user_posts.html', context)
