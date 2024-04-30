from rest_framework import serializers
from .models import ResearchPaper


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPaper
        fields = (
            "file",
            "uploaded_on",
        )


class ResearchPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPaper
        fields = (
            "id",
            "file",
            "uploaded_on",
        )
