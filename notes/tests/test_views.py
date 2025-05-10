from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from notes.models import Note


class NoteCRUDViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="viewuser", password="pass"
        )
        self.client.login(username="viewuser", password="pass")
        self.note = Note.objects.create(
            title="Initial Title",
            content="Initial Content",
            url="https://initial.com",
            author=self.user,
        )

    def test_note_list_view(self):
        response = self.client.get(reverse("notes:note-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Initial Title")

    def test_note_detail_view(self):
        response = self.client.get(
            reverse("notes:note-detail", args=[self.note.pk])
        )  # noqa: E501
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Initial Content")

    def test_note_create_view(self):
        response = self.client.post(
            reverse("notes:note-create"),
            {
                "title": "New Note",
                "content": "New Content",
                "url": "https://new.com",
            },  # noqa: E501
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="New Note").exists())

    def test_note_update_view(self):
        response = self.client.post(
            reverse("notes:note-edit", args=[self.note.pk]),
            {
                "title": "Updated Title",
                "content": "Updated Content",
                "url": "https://updated.com",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")

    def test_note_delete_view(self):
        response = self.client.post(
            reverse("notes:note-delete", args=[self.note.pk])
        )  # noqa: E501
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
