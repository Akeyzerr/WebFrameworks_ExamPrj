from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput
    (attrs={
        "placeholder": "Add new task",
    }))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = ['title', 'complete', 'tags']
