from django.urls import path

from .views import PdfUpload, VectorEmbedding

urlpatterns = [
    path("upload/", PdfUpload.as_view()),
    path("embedding/", VectorEmbedding.as_view()),
]
