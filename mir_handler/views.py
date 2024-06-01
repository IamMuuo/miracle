from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.mixins import Response, status

# Create your views here.


class Ping(APIView):
    """Returns pong."""

    def get(self, request, *args, **kwargs):
        return Response(
            {"message": "pong"},
            status=status.HTTP_200_OK,
        )
