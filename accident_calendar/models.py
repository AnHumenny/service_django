from django.db import models
from subtable.models import SubOrganization


class TimeSlot(models.Model):
    """TimeSlot model for managing time slots in the accident calendar.

    Stores date, start/end times, booking status, and related metadata.
    Ensures unique date and start time combinations, ordered by date and start time.
    """
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    number = models.CharField(null=True, blank=True)
    category = models.CharField(null=True, blank=True)
    sla = models.CharField(null=True, blank=True)
    city = models.CharField(null=True, blank=True)
    organization = models.ForeignKey(
        SubOrganization,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="organization_timeslots"
    )
    status = models.CharField(null=True, blank=True)
    booked_by = models.ForeignKey(SubOrganization, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['date', 'start_time']
        ordering = ['date', 'start_time']

    def __str__(self):
        return f"{self.date} {self.start_time}-{self.end_time}"


class Booking(models.Model):
    """Booking model for associating users with time slots.

    Links a time slot to a user (SubOrganization) and tracks booking creation time.
    """
    slot = models.ForeignKey(
        TimeSlot,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    user = models.ForeignKey(
        SubOrganization,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.slot.number} -> {self.user.name} -> {self.slot.date}"
                f" {self.slot.start_time}-{self.slot.end_time}")
