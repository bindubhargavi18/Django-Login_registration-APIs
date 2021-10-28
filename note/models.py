from django.db import models
from registration.models import UserDetails
# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
