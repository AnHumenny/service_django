from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

from accident.models import Accident
from accident_calendar.models import TimeSlot

@receiver(post_save, sender=Accident)
def create_timeslot_for_accident(sender, instance, created, **kwargs):
    """Creates a TimeSlot when a new Accident is saved.

    Populates TimeSlot with Accident's date, times, ID, city, category, and SLA.
    """

    if created:
        local_open = timezone.localtime(instance.datetime_open)

        TimeSlot.objects.create(
            date=local_open.date(),
            start_time=instance.datetime_open,
            end_time=instance.datetime_close if local_close else None,
            number=instance.id,
            city=instance.city,
            category=instance.category,
            sla=instance.sla,
            organization=instance.organization,
            status=instance.status,
            is_booked=False,
        )


@receiver(post_save, sender=Accident)
def update_timeslot_for_accident(sender, instance, created, **kwargs):
    """Updates existing TimeSlot when an Accident is updated.

    Syncs TimeSlot's date, times, and booking status with Accident's data.
    """
    if created:
        return

    qs = TimeSlot.objects.filter(number=instance.id)


    if instance.status == "close":
        qs.update(
            start_time=instance.datetime_open,
            end_time=instance.datetime_close,
            number=instance.id,
            city=instance.city,
            category=instance.category,
            sla=instance.sla,
            organization=instance.organization,
            status=instance.status,
            is_booked=True,
        )
    if instance.status == "check":
        qs.update(
            start_time=instance.datetime_open,
            end_time=instance.datetime_close,
            number=instance.id,
            city=instance.city,
            category=instance.category,
            sla=instance.sla,
            organization=instance.organization,
            status=instance.status,
            is_booked=False,
        )


@receiver(post_delete, sender=Accident)
def delete_timeslot_for_accident(sender, instance, **kwargs):
    """Deletes associated TimeSlot when an Accident is deleted.

    Removes TimeSlot with matching Accident ID.
    """

    TimeSlot.objects.filter(number=instance.id).delete()
