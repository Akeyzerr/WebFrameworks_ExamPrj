from django.urls import path
from . import views as homepage_views

urlpatterns = [
    path('', homepage_views.index, name="homepage"),
    # path('server_error_demo/', homepage_views.server_error_demo, name='500')
]