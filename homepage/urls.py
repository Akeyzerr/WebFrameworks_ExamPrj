from django.urls import path
from . import views as homepage_views

urlpatterns = [
    path('', homepage_views.index, name="homepage"),
]