from django.urls import path

from . import views as blog_views

urlpatterns = [
    path('', blog_views.index, name="blog-home"),
    # path('/upload', blog_views.DocumentCreateView, name="upload"),
    # path('create/', recipes_views.create, name="create_recipe"),
    # path('edit/<int:id>/', recipes_views.update, name="update_recipe"),
    # path('delete/<int:id>/', recipes_views.delete, name="delete_recipe"),
    # path('details/<int:id>/', recipes_views.details, name="recipe_details"),
]