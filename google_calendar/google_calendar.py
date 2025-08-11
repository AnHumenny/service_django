import requests
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from google_calendar.models import GoogleCalendarToken
from datetime import datetime, timezone

import logging
logger = logging.getLogger(__name__)


@login_required
def fetch_google_events(request):
    """Fetch upcoming Google Calendar events for the authenticated user."""
    try:
        token = GoogleCalendarToken.objects.get(user=request.user)
    except GoogleCalendarToken.DoesNotExist:
        return JsonResponse({"error": "Google token not found"}, status=404)

    headers = {
       "Authorization": f"Bearer {token.access_token}"
    }
    params = {
        "maxResults": 10,
        "singleEvents": True,
        "orderBy": "startTime",
        "timeMin": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    }
    response = requests.get(
        "https://www.googleapis.com/calendar/v3/calendars/primary/events",
        headers=headers,
        timeout=5,
        params=params
    )

    if response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch events", "details": response.json()},
                            status=response.status_code)

    events = response.json().get("items", [])
    return JsonResponse({"events": events})


def create_google_calendar_event(user, number, category, sla, problem, city, address, datetime_open, datetime_close,
                                 name, phone, description):
    """Create event in calendar Google."""
    try:
        token_obj = GoogleCalendarToken.objects.get(username=user)
    except GoogleCalendarToken.DoesNotExist:
        logger.warning(f"User {user} has not token Google Calendar")
        return {"error": "No Google Calendar token found for user"}

    access_token = token_obj.access_token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    resp = (
        f"Срок ликвидации аварии: {sla}\n"
        f"Проблема: {problem}\n"
        f"category: {category}\n"
        f"Город: {city}\n"
        f"Адрес: {address}\n"
        f"Имя: {name}\n"
        f"Телефон: {phone}\n"
        f"Описание: {description}\n"
    )

    body = {
        "summary": number,
        "description": resp,
        "start": {
            "dateTime": datetime_open.isoformat(),
            "timeZone": "Europe/Moscow",
        },
        "end": {
            "dateTime": datetime_close.isoformat(),
            "timeZone": "Europe/Moscow",
        },
    }

    logger.info(f"send event in Google: {body}")

    response = requests.post(
        "https://www.googleapis.com/calendar/v3/calendars/primary/events",
        headers=headers,
        timeout=5,
        json=body,
    )

    if response.status_code not in [200, 201]:
        logger.warning(f"Error Google API: {response.status_code} — {response.text}")
        return {"error": response.text}

    logger.info(f"Event created in Google Calendar: {response.json().get('htmlLink')}")
    return response.json()

def delete_google_calendar_event(user, google_event_id):
    """Delete event from google calendar."""
    try:
        token = GoogleCalendarToken.objects.get(username=user)
    except GoogleCalendarToken.DoesNotExist:
        logger.warning(f"Token not found for user {user}")
        return {"error": "Missing token"}

    access_token = token.access_token
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.delete(
        f"https://www.googleapis.com/calendar/v3/calendars/primary/events/{google_event_id}",
        headers=headers,
        timeout=10
    )

    if response.status_code != 204:
        logger.warning(f"Error deleting event: {response.status_code} — {response.text}")
        return {"error": response.text}

    logger.info(f"Deleted event {google_event_id} for user {user}")
    return {"status": "deleted"}
