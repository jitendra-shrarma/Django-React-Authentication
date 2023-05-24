# Import default modules
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Import Serializer from api.serializers
from .serializers import (
    UserSerializer,
    SignUpSerializer,
    SignInSerializer,
    SignOutSerializer,
)

# Import set_cookies from api.utils
from .utils import set_cookies, unset_cookies, get_access_token_response


# SignUpAPIView, used as_view for signup url,
class SignUpAPIView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        # Check for access_token and if request have access_token or refresh_token, return response
        response = get_access_token_response(request)
        if response:
            return response

        # Check validity of data, if it is not valid raise exceptions
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Create response, message and user info
        return Response(
            {
                "message": "Successfully signed up.",
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )


# SignInAPIView, used as_view for signin url,
class SignInAPIView(generics.GenericAPIView):
    serializer_class = SignInSerializer

    def post(self, request):
        # Check for access_token and if request have access_token or refresh_token, return response
        response = get_access_token_response(request)
        if response:
            return response

        # Check validity of data, if it is not valid raise exceptions
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.data

        # Authenticate User with username and password
        user = authenticate(
            request, username=user["username"], password=user["password"]
        )

        # If user is authenticated, create refresh_token from user_id
        if user:
            refresh_token = RefreshToken.for_user(user)

            # Create response, message and user info
            response = Response(
                {
                    "message": "Successfully signed-in.",
                    "user": UserSerializer(
                        user, context=self.get_serializer_context()
                    ).data,
                },
                status=status.HTTP_200_OK,
            )
            # Add tokens in cookies,
            set_cookies(response, refresh_token)
            return response

        # Return response with message "SignIn failed"
        return Response(
            {"message": "SignIn failed!"}, status=status.HTTP_204_NO_CONTENT
        )


# SignOutAPIView, used as_view for signout url,
class SignOutAPIView(generics.GenericAPIView):
    serializer_class = EmptySerializer

    def delete(self, request):
        # Check for access_token and if request have no access_token or refresh_token, return response
        response = get_access_token_response(request)
        if response is None:
            return Response(
                {"message": "Invalid request."}, status=status.HTTP_400_BAD_REQUEST
            )

        # Create response with message "Successfully signout."
        response = Response(
            {"message": "Successfully signout."}, status=status.HTTP_200_OK
        )
        # Remove tokens from cookies
        unset_cookies(response)
        return response
