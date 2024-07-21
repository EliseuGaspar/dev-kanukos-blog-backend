import jwt
from functools import wraps
from datetime import datetime, timedelta
from backend.settings import SECRET_KEY
from rest_framework import status
from rest_framework.response import Response

class JwtMiddleware():

    @classmethod
    def generateToken(cls, id: int, email: str, permission: str, access: str = None) -> str:
        payload = {
            'id': id,
            'email': email,
            'permission': permission,
            'access': access,
            'exp': (datetime.now() + timedelta(minutes = 5))
        }
        token = jwt.encode(payload, key = SECRET_KEY, algorithm = 'HS256')
        return token

    @classmethod
    def verifyToken(cls, token: str) -> bool:
        if not token:
            return Response({
                'response': None,
                'msg': 'Token Unsent'
            }, status = status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

            if data.get('permission') != 'admin':
                return Response({
                    'response': None,
                    'msg': 'Access denied. This is an admin route!'
                }, status = status.HTTP_401_UNAUTHORIZED)

            return True

        except jwt.exceptions.ExpiredSignatureError:
            return Response({
                'response': None,
                'msg': 'Session expired! Log back in.'
            }, status = status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)

        except jwt.exceptions.DecodeError:
            return Response({
                'response': None,
                'msg': 'Invalid token!'
            }, status = status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({
                'response': None,
                'msg': 'internal server error.',
            }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def tokenRequired(f):
        """Decorator to require token for authorization."""
        @wraps(f)
        def decorated(view_instance, request, *args, **kwargs):
            """Decorator function."""
            token = request.headers.get('Authorization')

            if not token:
                return Response({
                    'response': None,
                    'msg': 'Token Unsent'
                }, status = status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)

            try:
                data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

                if data.get('email'):
                    currentUser = {
                        'email': data.get('email'),
                        'id': data.get('id')
                    }
                else:
                    return Response({
                        'response': None,
                        'msg': 'Invalid token or invalid user'
                    }, status = status.HTTP_403_FORBIDDEN)
            
            except jwt.exceptions.ExpiredSignatureError:
                return Response({
                    'response': None,
                    'msg': 'Session expired! Log back in.'
                }, status = status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)
            
            except Exception as e:
                return Response({
                    'response': None,
                    'msg': 'internal server error.',
                }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

            kwargs['current_user'] = currentUser
            return f(view_instance, request, *args, **kwargs)
        return decorated

    @staticmethod
    def adminAccessOnly(f):
        """Decorator to require token for authorization."""
        @wraps(f)
        def decorated(view_instance, request, *args, **kwargs):
            """Decorator function."""
            token = request.headers.get('Authorization')

            if not token:
                return Response({
                    'response': None,
                    'msg': 'Token Unsent'
                }, status = status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)

            try:
                data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

                if data.get('permission') != 'admin':
                    return Response({
                        'response': None,
                        'msg': 'Access denied. This is an admin route!'
                    }, status = status.HTTP_401_UNAUTHORIZED)

                if data.get('email'):
                    currentUser = {
                        'email': data.get('email'),
                        'id': data.get('id')
                    }
                    access = data.get('access')
                else:
                    return Response({
                        'response': None,
                        'msg': 'Invalid token or invalid user'
                    }, status = status.HTTP_403_FORBIDDEN)
            
            except jwt.exceptions.ExpiredSignatureError:
                return Response({
                    'response': None,
                    'msg': 'Session expired! Log back in.'
                }, status = status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)
            
            except jwt.exceptions.DecodeError:
                return Response({
                    'response': None,
                    'msg': 'Invalid token!'
                }, status = status.HTTP_401_UNAUTHORIZED)
            
            except Exception as e:
                return Response({
                    'response': None,
                    'msg': 'internal server error.',
                }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

            kwargs['access'] = access
            kwargs['currentUser'] = currentUser
            return f(view_instance, request, *args, **kwargs)
        return decorated



