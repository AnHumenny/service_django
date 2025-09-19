import calendar
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from apps.accident_calendar.models import TimeSlot


def calendar_view(request):
    today = timezone.now().date()
    first_day = today.replace(day=1)
    last_day = first_day.replace(day=calendar.monthrange(first_day.year, first_day.month)[1])

    slots = TimeSlot.objects.filter(date__range=[first_day, last_day]).order_by('date', 'start_time')

    calendar_data = {}
    for slot in slots:
        date_str = slot.date.strftime('%Y-%m-%d')
        if date_str not in calendar_data:
            calendar_data[date_str] = []
        calendar_data[date_str].append(slot)

    context = {
        'calendar_data': calendar_data
    }
    return render(request, 'calendar/calendar.html', context)

@login_required
def book_slot(request, slot_id):
    slot = get_object_or_404(TimeSlot, id=slot_id)

    if slot.is_booked:
        return JsonResponse({'success': False, 'message': 'Слот уже забронирован.'}, status=400)

    slot.is_booked = True
    slot.booked_by = request.user
    slot.save()

    return JsonResponse({'success': True, 'message':
        f'Слот {slot.start_time.strftime("%H:%M")} - {slot.end_time.strftime("%H:%M")} успешно забронирован!'})
