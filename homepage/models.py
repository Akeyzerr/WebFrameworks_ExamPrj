from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class Entry(models.Model):
    TBI = "To be implemented."
    WIP = "Work in progress,"
    COMPLETED = "Completed."
    ENTRY_STATUS = (
        (TBI, "To be implemented"),
        (WIP, "Work in progress"),
        (COMPLETED, "Completed and functional"),
    )
    ENTRY_STATE = (
        ("Mandatory", "Mandatory"),
        ("Mandatory", "Optional")
    )

    title = models.CharField(max_length=255)
    requirement = models.TextField(max_length=255, null=True, blank=True)
    implementation = RichTextField()
    status = models.CharField(max_length=40, choices=ENTRY_STATUS)
    state = models.CharField(max_length=40, choices=ENTRY_STATE, default=None)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Quotes(models.Model):
    QUOTE_TAGS = (
        (True, 'Clean'),
        (False, 'Dirty'))
    clean_state = models.BooleanField(choices=QUOTE_TAGS, default=True)
    quote = models.CharField(max_length=140)

    def __str__(self):
        return self.quote
