# notes\urls.py

from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.NoteListView.as_view(), name="note-list"),
    path("<int:pk>/", views.NoteDetailView.as_view(), name="note-detail"),
    path("create/", views.NoteCreateView.as_view(), name="note-create"),
    path("<int:pk>/edit/", views.NoteUpdateView.as_view(), name="note-edit"),
    path(
        "<int:pk>/delete/", views.NoteDeleteView.as_view(), name="note-delete"
    ),  # noqa: E501
]
