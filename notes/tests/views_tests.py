import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from notes.models import Note


@pytest.mark.django_db
class TestNoteViews:
    def setup_method(self):
        self.user = User.objects.create_user(
            username="tester", password="pass"
        )  # noqa: E501
        self.client = Client()
        self.client.login(username="tester", password="pass")

    def test_create_note(self):
        url = reverse("notes:note-create")
        response = self.client.post(
            url,
            {
                "title": "New Note",
                "content": "Some text",
                "url": "https://example.com",
            },  # noqa: E501
        )
        assert response.status_code == 302
        assert Note.objects.filter(title="New Note").exists()

    def test_note_list(self):
        Note.objects.create(
            title="Note A", content="", url="", author=self.user
        )  # noqa: E501
        url = reverse("notes:note-list")
        response = self.client.get(url)
        assert response.status_code == 200
        assert "Note A" in response.content.decode()

    def test_update_note(self):
        note = Note.objects.create(
            title="Old", content="", url="", author=self.user
        )  # noqa: E501
        url = reverse("notes:note-edit", kwargs={"pk": note.pk})
        response = self.client.post(
            url,
            {
                "title": "Updated",
                "content": "New Content",
                "url": "https://example.com",
            },
        )
        assert response.status_code == 302
        note.refresh_from_db()
        assert note.title == "Updated"

    def test_delete_note(self):
        note = Note.objects.create(
            title="Delete Me", content="", url="", author=self.user
        )
        url = reverse("notes:note-delete", kwargs={"pk": note.pk})
        response = self.client.post(url)
        assert response.status_code == 302
        assert not Note.objects.filter(pk=note.pk).exists()
