# import os

from .models import ResearchPaper
from .embedding import (
    get_pdf_text,
    get_text_chunks,
    create_embedding,
    vector_store,
    search_query,
)

from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileUploadSerializer, ResearchPaperSerializer


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


class getPapers(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        papers = ResearchPaper.objects.all()
        serializer = ResearchPaperSerializer(papers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# os.environ.get("OPENAI_API_KEY")
class VectorEmbedding(APIView):
    index_name = "research-papers-index"
    namespace = "ns1"

    def post(self, request, *args, **kwargs):
        papers = ResearchPaper.objects.all()

        extracted_text = get_pdf_text(papers)
        text_chunks = get_text_chunks(extracted_text)

        embeddings = create_embedding(text_chunks)

        res = vector_store(embeddings, self.index_name, self.namespace)

        return Response(res, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        search_query("name of the university", self.index_name, self.namespace)
        return Response({"status": "success"}, status=status.HTTP_200_OK)
