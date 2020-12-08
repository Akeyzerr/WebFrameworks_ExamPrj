from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="todo-app"),
    path('update_task/<str:pk>/', TaskUpdateView.as_view(), name="update_task"),
    path('delete_task/<str:pk>/', TaskDeleteView.as_view(), name="delete")
]
