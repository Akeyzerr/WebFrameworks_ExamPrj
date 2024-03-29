from random import choice

from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from django.contrib import messages


def index(request):
    entries = Entry.objects.all().order_by('date_created')
    paginator = Paginator(entries, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        if request.user.profile.clean_quote_of_the_day:
            quotes = choice(Quotes.objects.filter(clean_state=request.user.profile.clean_quote_of_the_day))
        else:
            quotes = choice(Quotes.objects.all())
        messages.info(request, f"{quotes}")
    except AttributeError or IndexError:
        pass
    context = {
        "page_obj": page_obj,
    }
    return render(request, 'homepage/homepage_index.html', context)


def server_error_demo(request):
    return HttpResponseServerError('500.html')
