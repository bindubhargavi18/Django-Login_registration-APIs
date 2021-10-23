from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import FieldDoesNotExist, ValidationError
from django.db import IntegrityError
from django.http import JsonResponse
from .models import UserDetails
import json


def user_register(request):
    """
    This method register user by inheriting User Model into our own model.
    Using create_user method, storing details into database.
    Returns response whether user registered or not.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = UserDetails.objects.create_user(data.get('username'), data.get('email'), data.get('password'),
                                                   address=data.get('address'), city=data.get('city'),
                                                   state=data.get('state'))
            msg = {'message': 'new user registered successfully..'}
            return JsonResponse(msg)
        except IntegrityError:
            exception = {'Exception': 'Already exists...!'}
            return JsonResponse(exception)
        except Exception as e:
            exc = {'Exception': str(e)}
            return JsonResponse(exc)


def user_login(request):
    """
    This method logins based on username and password by using authenticate method.
    Returns response login is success or failed...
    """
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user is not None:
                data = {'message': 'successfully logged in..'}
                return JsonResponse(data)
            else:
                data = {'message': 'username or password is wrong..'}
                return JsonResponse(data)
    except ValidationError:
        exc_value = {'Exception': 'Values does not exists'}
        return JsonResponse(exc_value)
    except Exception as e:
        value = {'Exception': str(e)}
        return JsonResponse(value)
