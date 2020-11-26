from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'homepage/homepage_index.html', context)
