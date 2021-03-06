from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDetailsSerializer
import jwt


class Register(APIView):
    """
    This class registers new user based on the details...
    """
    def post(self, request):
        try:
            serializer = UserDetailsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "user registered successfully"}, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError:
            return Response("exception: username already exists!")

        except Exception as e:
            return Response({'exception': str(e)})


class Login(APIView):
    """
    This class creates login api and validate user based on details.
    Returns response of login success or fail.
    """
    def post(self, request):
        try:
            user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
            if user is not None:
                token = jwt.encode({"id": user.id}, 'secret', algorithm='HS256')
                return Response({"token": token})
            else:
                return Response({'message': "username or password is wrong..!"}, status=status.HTTP_400_BAD_REQUEST)

        except AuthenticationFailed:
            return Response("exception: Authentication failed..", status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({'exception': str(e)})
