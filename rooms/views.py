from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Room
from .serializers import ReadRoomSerializer

@api_view(["GET", "POST"])
def rooms_view(request):
    if request.method == "GET":
        rooms = Room.objects.all()
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)
    elif request.method == "POST":
        print(request.data)



class SeeRoomView(RetrieveAPIView):

    queryset = Room.objects.all()
    serializer_class = ReadRoomSerializer