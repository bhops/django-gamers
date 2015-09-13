from users.serializers import UserSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return {
            'token': token,
            'username': UserSerializer(user).data['username']
    }
