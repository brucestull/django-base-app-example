from django.test import TestCase
from django.contrib.auth import get_user_model
from notes.models import Note


class NoteModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="pass"
        )
        self.note = Note.objects.create(
            title="Test Note",
            content="Test Content",
            url="https://example.com",
            author=self.user,
        )

    def test_str_representation(self):
        self.assertEqual(str(self.note), "Test Note")

    def test_note_fields(self):
        self.assertEqual(self.note.content, "Test Content")
        self.assertEqual(self.note.author, self.user)
