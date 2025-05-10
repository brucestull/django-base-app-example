import pytest
from notes.models import Note
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_dunder_str_method():
    user_bob = get_user_model().objects.create_user(
        username="bob", password="pass"
    )  # noqa: E501
    bobs_note = Note.objects.create(
        title="Hello", content="World", author=user_bob
    )  # noqa: E501
    assert str(bobs_note) == "Hello"
