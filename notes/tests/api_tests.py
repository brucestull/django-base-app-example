import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from notes.models import Note


@pytest.mark.django_db
class TestNoteAPI:
    def setup_method(self):
        self.user = User.objects.create_user(
            username="apiuser", password="pass"
        )  # noqa: E501
        self.client = APIClient()
        self.client.login(username="apiuser", password="pass")

    def test_create_note_api(self):
        response = self.client.post(
            "/api/notes/",
            {
                "title": "API Note",
                "content": "REST Content",
                "url": "https://api.com",
            },  # noqa: E501
        )
        assert response.status_code == 201
        assert Note.objects.filter(title="API Note").exists()

    def test_list_notes_api(self):
        Note.objects.create(
            title="NoteX", content="...", url="", author=self.user
        )  # noqa: E501
        response = self.client.get("/api/notes/")
        assert response.status_code == 200
        assert any(note["title"] == "NoteX" for note in response.json())

    def test_update_note_api(self):
        note = Note.objects.create(
            title="UpMe", content="...", url="", author=self.user
        )
        response = self.client.patch(
            f"/api/notes/{note.pk}/", {"title": "Updated API"}
        )  # noqa: E501
        assert response.status_code == 200
        note.refresh_from_db()
        assert note.title == "Updated API"

    def test_delete_note_api(self):
        note = Note.objects.create(
            title="ZapMe", content="...", url="", author=self.user
        )
        response = self.client.delete(f"/api/notes/{note.pk}/")
        assert response.status_code == 204
        assert not Note.objects.filter(pk=note.pk).exists()
