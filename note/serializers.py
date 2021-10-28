from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)

    class Meta:
        model = Note
        fields = "__all__"
