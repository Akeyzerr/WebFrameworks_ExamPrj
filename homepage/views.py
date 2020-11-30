from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Entry


def index(request):
    entries = Entry.objects.all().order_by('date_created')
    paginator = Paginator(entries, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, 'homepage/homepage_index.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html', exception)


def server_error_view(request):
    return render(request, '500.html')


def permission_denied_view(request, exception):
    return render(request, '403.html', exception)
