from django.core.exceptions import FieldDoesNotExist, ValidationError
from django.http import JsonResponse
from .models import Register
import json


def user_register(request):
    """
    This method register registration details and return response whether registration is registered or not
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            user_data = {
                'user_name': data.get('user_name'),
                'first_name': data.get('first_name'),
                'last_name': data.get('last_name'),
                'password': data.get('password')
                }
            if Register.objects.filter(user_name=data.get('user_name')):
                data = {'message': 'username already exists..'}
                return JsonResponse(data)
            else:
                user = Register.objects.create(**user_data)
                data = {'Message': 'New registration registered successfully..'}
                return JsonResponse(data)
        except FieldDoesNotExist:
            exception = {'Exception': 'Field does not exists..'}
            return JsonResponse(exception)
        except Exception as e:
            exc = {'Exception': str(e)}
            return JsonResponse(exc)


def user_login(request):
    """
    This method logins registration based on username and password.
    Returns login success or failed...
    """
    try:
        data = json.loads(request.body)
        if Register.objects.filter(user_name=data.get('user_name'), password=data.get('password')):
            success_data = {'message': 'Login successful'}
            return JsonResponse(success_data)
        else:
            fail_data = {'message': 'Invalid username or password...!'}
            return JsonResponse(fail_data)
    except ValidationError:
        exc_value = {'Exception': 'Values does not exists'}
        return JsonResponse(exc_value)
    except Exception as e:
        value = {'Exception': str(e)}
        return JsonResponse(value)
