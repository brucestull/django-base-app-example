from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from notes.models import Note


class NoteAPITest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="apiuser", password="pass"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.note = Note.objects.create(
            title="API Note",
            content="API Content",
            url="https://api.com",
            author=self.user,
        )

    def test_list_notes_api(self):
        response = self.client.get("/api/notes/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("API Note", response.content.decode())

    def test_create_note_api(self):
        response = self.client.post(
            "/api/notes/",
            {
                "title": "Created via API",
                "content": "API-generated content",
                "url": "https://newapi.com",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Note.objects.filter(title="Created via API").exists())

    def test_update_note_api(self):
        response = self.client.patch(
            f"/api/notes/{self.note.pk}/", {"title": "Patched Title"}
        )
        self.assertEqual(response.status_code, 200)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Patched Title")

    def test_delete_note_api(self):
        response = self.client.delete(f"/api/notes/{self.note.pk}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
