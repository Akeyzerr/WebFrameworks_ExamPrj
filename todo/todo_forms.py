from django import forms
from django.forms import ModelForm
from django_currentuser.middleware import get_current_authenticated_user

from .models import *


# class TaskForm(forms.ModelForm):
#     title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Add new task"}))
#     user = get_current_authenticated_user()
#
#     class Meta:
#         model = Task
#         fields = ['title', 'user']
