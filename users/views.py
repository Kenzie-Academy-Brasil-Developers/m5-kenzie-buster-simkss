from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .serializers import RegisterSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAuthUser
from .models import User
from django.shortcuts import get_object_or_404

# Create your views here.
class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,  status=status.HTTP_201_CREATED)

class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthUser]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        serializer = RegisterSerializer(user)

        if request.user.is_employee != True:
            if request.user.id == user.id:
                return Response(serializer.data)

            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

        return Response(serializer.data)



# Create your views here.
