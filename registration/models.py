from django.contrib.auth.models import User
from django.db import models


class UserDetails(User):
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
