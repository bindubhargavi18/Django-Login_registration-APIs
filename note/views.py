from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import NoteSerializer
from .models import Note
from utility import verify_token


class NoteModel(APIView):

    @verify_token
    def post(self, request):
        """
        This method creates a note for particular user id.
        Returns note is created or not.
        """
        try:
            serializer = NoteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": 'note is added successfully..!',
                     'data': {'note list': serializer.data}}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'exception_Message': str(e)})

    @verify_token
    def get(self, request):
        """
        This method displays the note data based on the user_id.
        """

        try:
            note = Note.objects.filter(user_id=request.data.get('user_id'))
            serializer = NoteSerializer(note, many=True)
            return Response(
                {"message": 'note for user:',
                 'data': {'note list': serializer.data}}, status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
            return Response({"error": f"user_id:{request.data.get('user_id')} does not exist!"})

        except Exception as e:
            return Response({"exception": str(e)})

    @verify_token
    def delete(self, request):
        """
        This method deletes the entire note record based on
        the note id(primary key) of table note.
        """
        try:
            note = Note.objects.get(id=request.data.get('id'))
            note.delete()
            return Response({"message": "record has been deleted..!"})

        except ObjectDoesNotExist:
            return Response({"error": " does not exists..!"})

        except Exception as e:
            return Response({"exception": str(e)})

    @verify_token
    def put(self, request):
        """
        This method updates the data in note app for particular note id.
        """
        try:
            note = Note.objects.get(id=request.data.get('id'))
            serializer = NoteSerializer(note, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "record has been updated successfully..!",
                                 'data': {'note list': serializer.data}}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'exception_message': str(e)})
