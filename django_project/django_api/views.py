from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *

# Create your views here.

@api_view(['GET', 'POST'])
def account_data(request):
    if request.method == 'GET':
        data = PVE.objects.all()
        serializer = PVESerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('post')
        serializer = PVESerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def delete_account(request, id):
    try:
        student = PVE.objects.get(id=id)
    except PVE.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = PVESerializer(student, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TokenView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        try:
            refresh_token = request.data["refresh_token"]
            р = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)