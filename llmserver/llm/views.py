from .models import ResearchPaper

from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileUploadSerializer


class PdfUpload(APIView):
    parser_classes = (MultiPartParser,)
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VectorEmbedding(APIView):
    def get(self, request, *args, **kwargs):
        try:
            paper = ResearchPaper.objects.get(pk=1)
        except ResearchPaper.DoesNotExist:
            return Response(
                {"error": "Paper not found"}, status=status.HTTP_404_NOT_FOUND
            )

        pdf_path = paper.file.path

        print(pdf_path)

        return Response("pdf_bytes", status=status.HTTP_200_OK)
