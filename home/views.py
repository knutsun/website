from django.shortcuts import render
from events.models import Event


def index(request):

    all_events = Event.objects.all()
    event_count = all_events.count()
    three_events = all_events.order_by('date')[:3]

    context = {
        'all_events': all_events,
        'event_count': event_count,
        'three_events': three_events,
    }

    return render(request, 'index.html', context)
