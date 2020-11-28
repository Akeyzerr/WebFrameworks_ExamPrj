from django.shortcuts import render
from django_currentuser.middleware import get_current_authenticated_user

from .models import Entry


def index(request):
    author = get_current_authenticated_user()
    entries = Entry.objects.all().order_by('pk')
    context = {
        "author": author,
        "entries": entries,
    }
    return render(request, 'homepage/homepage_index.html', context)
