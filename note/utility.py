import jwt
from rest_framework.response import Response


def verify_token(function):
    def wrapper(self, request):
        try:
            if 'HTTP_AUTHORIZATION' not in request.META:
                resp = Response({'message': 'Token Not provided in header'})
                resp.status_code = 400
                return resp
            decoded_token = jwt.decode(request.META.get('HTTP_AUTHORIZATION'), 'secret', algorithms='HS256')
            request.data["user_id"] = decoded_token.get("user_id")
            return function(self, request)
        except Exception as e:
            return Response({'Exception': str(e)})

    return wrapper
