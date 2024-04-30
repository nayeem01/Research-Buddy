from django.urls import path

from .views import PdfUpload, VectorEmbedding, getPapers

urlpatterns = [
    path("upload/", PdfUpload.as_view()),
    path("get-papers/", getPapers.as_view()),
    path("embedding/", VectorEmbedding.as_view()),
]
