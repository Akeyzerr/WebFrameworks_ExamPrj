from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *


def index(request):
    return render(request, 'blog/index.html')


class DocumentCreateView(CreateView):
    model = Document
    fields = ['upload', ]
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context