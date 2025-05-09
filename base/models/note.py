# base/models/note.py

from django.db import models
from django.contrib.auth import get_user_model


class NoteBase(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    url = models.URLField(blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_notes",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
