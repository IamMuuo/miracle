from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.mixins import Response, status

from miracle.MIRFile import MIRFile
from .serializers import MIRModelFileSerializer

# Create your views here.


class Ping(APIView):
    """Returns pong."""

    def get(self, request, *args, **kwargs):
        return Response(
            {"message": "pong"},
            status=status.HTTP_200_OK,
        )

    def post(self, request, *args, **kwargs):
        file_serializer = MIRModelFileSerializer(data=request.data)
        if file_serializer.is_valid():
            mir_file: InMemoryUploadedFile = request.FILES["mir_file"]
            file_serializer.save()

            print(type(mir_file))
            file_to_parse = MIRFile("")

            try:
                file_bytes = file_to_parse.read_in_memory_file_bytes(mir_file)
                if file_bytes is not None:
                    return Response(
                        file_to_parse.parse(file_bytes),
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    return Response(
                        {"error": "Filaed to  read MIR file read_bytes"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
