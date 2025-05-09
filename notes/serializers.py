# notes\serializers.py

from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "url", "author", "created", "updated"]
        read_only_fields = ["author", "created", "updated"]
