from django.urls import path

from .views import PdfUpload

urlpatterns = [
    path("upload/", PdfUpload.as_view()),
]
