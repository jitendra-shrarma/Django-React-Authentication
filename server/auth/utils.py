# Import RefreshToken, Response and status
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


# Set refresh_token in COOKIES for 24 hours
def set_refresh_token(response, refresh_token=None):
    if refresh_token:
        response.set_cookie(
            "refresh_token", refresh_token, httponly=True, max_age=(24 * 3600)
        )


# Set access_token in COOKIES for 30 minutes
def set_access_token(response, refresh_token=None):
    if refresh_token:
        response.set_cookie(
            "access_token", refresh_token.access_token, httponly=True, max_age=(1800)
        )


# Get refresh_token_str from COOKIES
def get_refresh_token(request):
    refresh_token_str = request.COOKIES.get("refresh_token", None)
    if refresh_token_str is not None:
        return refresh_token_str
    return None


# Get access_token_str from COOKIES
def get_access_token(request):
    access_token_str = request.COOKIES.get("access_token", None)
    if access_token_str is not None:
        return access_token_str
    return None


# Set access_token and refresh_token in COOKIES
def set_cookies(response, refresh_token=None):
    set_access_token(response, refresh_token)
    set_refresh_token(response, refresh_token)


# Remove access_token and refresh_token from COOKIES
def unset_cookies(response):
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")


# Check request for access_token
def get_access_token_response(request=None):
    # If it's a request
    if request:
        access_token = get_access_token(request)
        # And if Request have access_token,
        if access_token:
            # Create "Invalid request" response and return
            response = Response(
                {"message": "Invalid request."}, status=status.HTTP_400_BAD_REQUEST
            )
            return response

        # If request have no access_token, check for refresh token
        refresh_token = get_refresh_token(request)
        # If Request have refresh token,
        if refresh_token:
            # Create "Invalid request" response and create a new access_token
            response = Response(
                {"message": "Invalid request."}, status=status.HTTP_400_BAD_REQUEST
            )
            set_access_token(response, RefreshToken(refresh_token))
            return response

    # If no request is made, return no response
    return None
