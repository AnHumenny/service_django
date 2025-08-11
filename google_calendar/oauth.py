import requests
from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from google_calendar.models import GoogleCalendarToken
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

import os


CLIENT_ID = settings.GOOGLE_CLIENT_ID
CLIENT_SECRET = settings.GOOGLE_CLIENT_SECRET
REDIRECT_URI = settings.GOOGLE_OAUTH_REDIRECT_URI

def start_google_auth(request):
    """Initiate the Google OAuth2 authorization flow for calendar access."""
    if request.user.is_authenticated:
        request.session["oauth_user_id"] = request.user.id
        logger.info(f"Saved user_id {request.user.id} in session")
    else:
        logger.warning("User is not authenticated in start_google_auth")
    auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth?"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={REDIRECT_URI}&"
        "response_type=code&"
        "scope=https://www.googleapis.com/auth/calendar.events https://www.googleapis.com/auth/calendar.readonly&"
        "access_type=offline&prompt=consent"
    )

    return redirect(auth_url)


@csrf_exempt
def google_calendar_callback(request):
    """Handle the OAuth2 callback from Google Calendar."""
    code = request.GET.get("code")
    if not code:
        return JsonResponse({"error": "Missing code in request"}, status=400)

    token_url = settings.GOOGLE_OAUTH_TOKEN_URL

    data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data, timeout=5)
    token_data = response.json()

    if "access_token" not in token_data:
        return JsonResponse({"error": token_data}, status=400)

    access_token = token_data["access_token"]
    refresh_token = token_data.get("refresh_token")
    expires_in = token_data.get("expires_in")

    user_id = request.session.get("oauth_user_id")
    if not user_id:
        return JsonResponse({"error": "User session not found"}, status=401)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    GoogleCalendarToken.objects.update_or_create(
        username=user,
        defaults={
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_in": expires_in,
        },
    )

    return HttpResponseRedirect("/")
