from django.urls import path
from note.views import NoteModel


urlpatterns = [
    path('note/', NoteModel.as_view(), name="note")
    # path('note/login', Login.as_view())
]
