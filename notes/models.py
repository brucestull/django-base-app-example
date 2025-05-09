# notes/models.py

from base.models import NoteBase


class Note(NoteBase):
    """
    Concrete implementation of NoteBase.
    """

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
