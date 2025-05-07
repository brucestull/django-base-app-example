# Django Abstract Base Model

- [Django Abstract Base Model - Share](https://chatgpt.com/share/681b69c7-18b8-8002-9100-587dd1a54a01)
- [Django Abstract Base Model - Private](https://chatgpt.com/c/681b6723-99f0-8002-817d-870154f2dcb5)

We've been talking in other chats about Django Base classes for abstract use.

I like the convention of `NoteBase` in `base/models/note.py`.

Can you provide a simple django app with a base app `base/models/note.py` with abstract model `NoteBase` and add a simple `notes` app which uses that base?

Absolutely! Here's a clear example of how to structure a Django project with a reusable abstract base model in a `base` app, and a concrete implementation in a `notes` app.

---

### 🧱 Project Structure Overview

```
myproject/
├── base/
│   ├── __init__.py
│   └── models/
│       ├── __init__.py
│       └── note.py  ← NoteBase lives here
├── notes/
│   ├── __init__.py
│   ├── models.py    ← Inherits from NoteBase
│   └── admin.py
├── manage.py
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

### ✅ Step 1: `base/models/note.py`

```python
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
        related_name="%(app_label)s_%(class)s_notes"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
```

---

### ✅ Step 2: `base/models/__init__.py`

```python
from .note import NoteBase
```

---

### ✅ Step 3: `notes/models.py`

```python
# notes/models.py

from base.models import NoteBase


class Note(NoteBase):
    """
    Concrete implementation of NoteBase.
    """

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
```

---

### ✅ Step 4: `notes/admin.py`

```python
from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created")
```

---

### ✅ Step 5: `myproject/settings.py`

Make sure both apps are registered:

```python
INSTALLED_APPS = [
    ...
    "base",
    "notes",
]
```

---

Let me know if you want a `forms.py`, serializer, views, or migrations added as well. Want a GitHub-style zipped repo or ready-to-copy starter repo structure?

Add `forms.py`, vanilla django CRUD views, and Django REST CRUD endpoints.

I'll copy and paste so no need for a zip.

Perfect! Here's the full setup with:

* ✅ `forms.py` in `notes/`
* ✅ Vanilla Django CRUD views
* ✅ Django REST Framework CRUD endpoints (with router)

---

## 🔹 `notes/forms.py`

```python
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "url"]
```

---

## 🔹 `notes/views.py` (Vanilla Django CRUD)

```python
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Note
from .forms import NoteForm


class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"


class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/note_detail.html"


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("notes:note-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("notes:note-list")


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("notes:note-list")
```

---

## 🔹 `notes/urls.py`

```python
from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.NoteListView.as_view(), name="note-list"),
    path("<int:pk>/", views.NoteDetailView.as_view(), name="note-detail"),
    path("create/", views.NoteCreateView.as_view(), name="note-create"),
    path("<int:pk>/edit/", views.NoteUpdateView.as_view(), name="note-edit"),
    path("<int:pk>/delete/", views.NoteDeleteView.as_view(), name="note-delete"),
]
```

---

## 🔹 `notes/serializers.py`

```python
from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "url", "author", "created", "updated"]
        read_only_fields = ["author", "created", "updated"]
```

---

## 🔹 `notes/api_views.py` (DRF ViewSet)

```python
from rest_framework import viewsets, permissions
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

---

## 🔹 `notes/api_urls.py` (DRF Router)

```python
from rest_framework.routers import DefaultRouter
from .api_views import NoteViewSet

router = DefaultRouter()
router.register(r"notes", NoteViewSet, basename="note")

urlpatterns = router.urls
```

---

## 🔹 Main `urls.py` in project (e.g., `myproject/urls.py`)

```python
from django.contrib import admin
from django.urls import path, include
from notes import urls as notes_urls
from notes.api_urls import urlpatterns as notes_api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("notes/", include(notes_urls)),
    path("api/", include(notes_api_urls)),
    path("api-auth/", include("rest_framework.urls")),  # for browsable API login
]
```

---

Do you want example HTML templates next (`note_list.html`, etc.) or DRF token authentication setup?

Provide all of those.

Awesome. Here’s **everything else you asked for**:

---

## ✅ Django Templates for CRUD views (`notes/templates/notes/`)

---

### 🔸 `note_list.html`

```html
{% extends "base.html" %}

{% block content %}
  <h1>All Notes</h1>
  <a href="{% url 'notes:note-create' %}">Create New Note</a>
  <ul>
    {% for note in object_list %}
      <li>
        <a href="{% url 'notes:note-detail' note.pk %}">{{ note.title }}</a> by {{ note.author }}
      </li>
    {% endfor %}
  </ul>
{% endblock %}
```

---

### 🔸 `note_detail.html`

```html
{% extends "base.html" %}

{% block content %}
  <h2>{{ object.title }}</h2>
  <p>{{ object.content }}</p>
  <p>URL: <a href="{{ object.url }}">{{ object.url }}</a></p>
  <p>Author: {{ object.author }}</p>
  <a href="{% url 'notes:note-edit' object.pk %}">Edit</a> |
  <a href="{% url 'notes:note-delete' object.pk %}">Delete</a> |
  <a href="{% url 'notes:note-list' %}">Back to List</a>
{% endblock %}
```

---

### 🔸 `note_form.html`

```html
{% extends "base.html" %}

{% block content %}
  <h2>{% if form.instance.pk %}Edit Note{% else %}Create Note{% endif %}</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
  </form>
  <a href="{% url 'notes:note-list' %}">Cancel</a>
{% endblock %}
```

---

### 🔸 `note_confirm_delete.html`

```html
{% extends "base.html" %}

{% block content %}
  <h2>Delete "{{ object.title }}"?</h2>
  <form method="post">
    {% csrf_token %}
    <button type="submit">Yes, delete</button>
  </form>
  <a href="{% url 'notes:note-detail' object.pk %}">Cancel</a>
{% endblock %}
```

---

## ✅ Minimal `base.html`

Place this in `templates/base.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django Notes</title>
</head>
<body>
    {% if user.is_authenticated %}
        <p>Welcome, {{ user.username }} | <a href="{% url 'logout' %}">Logout</a></p>
    {% else %}
        <p><a href="{% url 'login' %}">Login</a></p>
    {% endif %}

    {% block content %}
    {% endblock %}
</body>
</html>
```

---

## ✅ DRF Token Authentication

---

### 🔸 Install the package (if needed)

```bash
pip install djangorestframework
pip install djangorestframework-simplejwt
```

---

### 🔸 Add to `settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ]
}
```

---

### 🔸 Create tokens for users (via admin or shell)

```bash
python manage.py drf_create_token <username>
```

Or in `urls.py`:

```python
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns += [
    path("api/token-auth/", obtain_auth_token),
]
```

Clients can `POST` username and password to `/api/token-auth/` and use:

```
Authorization: Token <your_token>
```

---

## ✅ Optional: Login/Logout URLs for Browsable API and Site

Add to your main `urls.py`:

```python
urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),  # login/logout for views
    path("api-auth/", include("rest_framework.urls")),        # login/logout for API
]
```

---

Would you like me to generate some sample test data or fixtures next?

yes, and add full-coverage testing.

Excellent. Let’s add:

---

## ✅ 1. Sample Test Data (Fixture)

Create a file `notes/fixtures/test_users_and_notes.json`:

```json
[
  {
    "model": "auth.user",
    "pk": 1,
    "fields": {
      "username": "alice",
      "password": "pbkdf2_sha256$260000$X$Y",  # Replace with real hash or use createsuperuser
      "is_superuser": true,
      "is_staff": true
    }
  },
  {
    "model": "notes.note",
    "pk": 1,
    "fields": {
      "title": "Test Note",
      "content": "This is a test note.",
      "url": "https://example.com",
      "author": 1,
      "created": "2024-01-01T00:00:00Z",
      "updated": "2024-01-01T00:00:00Z"
    }
  }
]
```

Load it with:

```bash
python manage.py loaddata test_users_and_notes.json
```

Or use `User.objects.create_user()` in test setup.

---

## ✅ 2. Full Coverage Testing (Django + DRF)

Create `notes/tests/test_views.py`, `test_api.py`, and `test_models.py`.

---

### 🔹 `notes/tests/test_models.py`

```python
import pytest
from notes.models import Note
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_str_method():
    user = get_user_model().objects.create_user(username="bob", password="pass")
    note = Note.objects.create(title="Hello", content="World", author=user)
    assert str(note) == "Hello"
```

---

### 🔹 `notes/tests/test_views.py`

```python
import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from notes.models import Note


@pytest.mark.django_db
class TestNoteViews:
    def setup_method(self):
        self.user = User.objects.create_user(username="tester", password="pass")
        self.client = Client()
        self.client.login(username="tester", password="pass")

    def test_create_note(self):
        url = reverse("notes:note-create")
        response = self.client.post(url, {
            "title": "New Note",
            "content": "Some text",
            "url": "https://example.com"
        })
        assert response.status_code == 302
        assert Note.objects.filter(title="New Note").exists()

    def test_note_list(self):
        Note.objects.create(title="Note A", content="", url="", author=self.user)
        url = reverse("notes:note-list")
        response = self.client.get(url)
        assert response.status_code == 200
        assert "Note A" in response.content.decode()

    def test_update_note(self):
        note = Note.objects.create(title="Old", content="", url="", author=self.user)
        url = reverse("notes:note-edit", kwargs={"pk": note.pk})
        response = self.client.post(url, {
            "title": "Updated",
            "content": "New Content",
            "url": "https://example.com"
        })
        assert response.status_code == 302
        note.refresh_from_db()
        assert note.title == "Updated"

    def test_delete_note(self):
        note = Note.objects.create(title="Delete Me", content="", url="", author=self.user)
        url = reverse("notes:note-delete", kwargs={"pk": note.pk})
        response = self.client.post(url)
        assert response.status_code == 302
        assert not Note.objects.filter(pk=note.pk).exists()
```

---

### 🔹 `notes/tests/test_api.py`

```python
import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from notes.models import Note


@pytest.mark.django_db
class TestNoteAPI:
    def setup_method(self):
        self.user = User.objects.create_user(username="apiuser", password="pass")
        self.client = APIClient()
        self.client.login(username="apiuser", password="pass")

    def test_create_note_api(self):
        response = self.client.post("/api/notes/", {
            "title": "API Note",
            "content": "REST Content",
            "url": "https://api.com"
        })
        assert response.status_code == 201
        assert Note.objects.filter(title="API Note").exists()

    def test_list_notes_api(self):
        Note.objects.create(title="NoteX", content="...", url="", author=self.user)
        response = self.client.get("/api/notes/")
        assert response.status_code == 200
        assert any(note["title"] == "NoteX" for note in response.json())

    def test_update_note_api(self):
        note = Note.objects.create(title="UpMe", content="...", url="", author=self.user)
        response = self.client.patch(f"/api/notes/{note.pk}/", {
            "title": "Updated API"
        })
        assert response.status_code == 200
        note.refresh_from_db()
        assert note.title == "Updated API"

    def test_delete_note_api(self):
        note = Note.objects.create(title="ZapMe", content="...", url="", author=self.user)
        response = self.client.delete(f"/api/notes/{note.pk}/")
        assert response.status_code == 204
        assert not Note.objects.filter(pk=note.pk).exists()
```

---

## ✅ 3. Run Tests and Measure Coverage

Install if needed:

```bash
pip install pytest pytest-django pytest-cov
```

Set up `pytest.ini`:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = myproject.settings
python_files = tests.py test_*.py *_tests.py
```

Run tests with coverage:

```bash
pytest --cov=notes --cov-report=term-missing
```

---

Would you like to automate test running via GitHub Actions, or add Selenium/browser tests next?

Can you provide code for full-coverage `unittest`?

Absolutely. Below is a full suite of **Django `unittest.TestCase`-style tests** covering:

* ✅ `Note` model
* ✅ CRUD class-based views (`NoteListView`, `NoteDetailView`, etc.)
* ✅ Django REST Framework ViewSet endpoints

All in classic `unittest` style, aiming for **100% coverage** of all code paths.

---

## ✅ `notes/tests/test_models.py`

```python
from django.test import TestCase
from django.contrib.auth import get_user_model
from notes.models import Note


class NoteModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="pass")
        self.note = Note.objects.create(
            title="Test Note",
            content="Test Content",
            url="https://example.com",
            author=self.user
        )

    def test_str_representation(self):
        self.assertEqual(str(self.note), "Test Note")

    def test_note_fields(self):
        self.assertEqual(self.note.content, "Test Content")
        self.assertEqual(self.note.author, self.user)
```

---

## ✅ `notes/tests/test_views.py`

```python
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from notes.models import Note


class NoteCRUDViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username="viewuser", password="pass")
        self.client.login(username="viewuser", password="pass")
        self.note = Note.objects.create(
            title="Initial Title",
            content="Initial Content",
            url="https://initial.com",
            author=self.user
        )

    def test_note_list_view(self):
        response = self.client.get(reverse("notes:note-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Initial Title")

    def test_note_detail_view(self):
        response = self.client.get(reverse("notes:note-detail", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Initial Content")

    def test_note_create_view(self):
        response = self.client.post(reverse("notes:note-create"), {
            "title": "New Note",
            "content": "New Content",
            "url": "https://new.com"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="New Note").exists())

    def test_note_update_view(self):
        response = self.client.post(reverse("notes:note-edit", args=[self.note.pk]), {
            "title": "Updated Title",
            "content": "Updated Content",
            "url": "https://updated.com"
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")

    def test_note_delete_view(self):
        response = self.client.post(reverse("notes:note-delete", args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
```

---

## ✅ `notes/tests/test_api.py`

```python
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from notes.models import Note


class NoteAPITest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="apiuser", password="pass")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.note = Note.objects.create(
            title="API Note",
            content="API Content",
            url="https://api.com",
            author=self.user
        )

    def test_list_notes_api(self):
        response = self.client.get("/api/notes/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("API Note", response.content.decode())

    def test_create_note_api(self):
        response = self.client.post("/api/notes/", {
            "title": "Created via API",
            "content": "API-generated content",
            "url": "https://newapi.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Note.objects.filter(title="Created via API").exists())

    def test_update_note_api(self):
        response = self.client.patch(f"/api/notes/{self.note.pk}/", {
            "title": "Patched Title"
        })
        self.assertEqual(response.status_code, 200)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Patched Title")

    def test_delete_note_api(self):
        response = self.client.delete(f"/api/notes/{self.note.pk}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
```

---

## ✅ Run with Coverage

Install test tools if needed:

```bash
pip install coverage
```

Then:

```bash
coverage run manage.py test
coverage report -m
```

---

Do you want:

* GitHub Actions workflow for auto-running tests?
* Or `setUpTestData` instead of `setUp` for performance boost?

Let me know!
