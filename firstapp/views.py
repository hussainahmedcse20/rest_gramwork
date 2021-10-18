from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer


@api_view(['POST'])
def register_view(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully Done"
            data['username'] = user.username
            data['email'] = user.email
        else:
            data=serializer.errors
        return Response(data)
