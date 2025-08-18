from celery import shared_task
from django.core.mail import send_mail
from decouple import config

@shared_task
def send_accident_email(accident_id, email_data):
    """Send email asynchronously."""
    try:
        send_mail(
            subject=email_data['subject'],
            message=email_data['message'],
            from_email=config('EMAIL_HOST_USER'),
            recipient_list=[email_data['recipient']],
            fail_silently=False,
        )
        return f"Email sent for accident {accident_id}"
    except Exception as e:
        return f"Failed to send email for accident {accident_id}: {str(e)}"
