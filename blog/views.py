from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *

# class DocumentCreateView(CreateView):
#     model = Document
#     fields = ['upload', ]
#     success_url = reverse_lazy('home')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         documents = Document.objects.all()
#         context['documents'] = documents
#         return context


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_public=True).order_by('-date_edited')
    template_name = 'blog/index.html'
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(is_public=True)


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
