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


def page_not_found_view(request, exception):
    return render(request, '404.html', exception)


def server_error_view(request):
    return render(request, '500.html')


def permission_denied_view(request, exception):
    return render(request, '403.html', exception)
