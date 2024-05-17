from rest_framework import generics, permissions
from accounts.serializers import RegisterSerializer, LoginInSerializer
from rest_framework.response import Response


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny, ]


    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LoginAPIView(generics.GenericAPIView):

    serializer_class = LoginInSerializer
    permission_classes = [permissions.AllowAny,]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
