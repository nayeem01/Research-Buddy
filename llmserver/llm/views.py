from .models import ResearchPaper
from .embedding import get_pdf_text, get_text_chunks

from langchain_community.embeddings import HuggingFaceInstructEmbeddings

model = "hkunlp/instructor-xl"


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
    def get(self, request, *args, **kwargs):
        papers = ResearchPaper.objects.all()

        extracted_text = get_pdf_text(papers)
        text_chunks = get_text_chunks(extracted_text)

        return Response(text_chunks, status=status.HTTP_200_OK)
