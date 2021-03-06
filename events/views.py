import calendar
import datetime

from django.shortcuts import render
from django.views.generic import DetailView

from .models import Event


def index(request):
    all_events = Event.objects.all()
    event_count = all_events.count()
    now = datetime.datetime.now()
    current_month_str = now.strftime("%B")
    current_month = now.month
    current_year = now.year
    cal = calendar.Calendar()
    days = cal.itermonthdays2(current_year, current_month)

    date_list = [day for day in days]
    days_in_date_list = []

    for x, y in date_list:
        days_in_date_list.append(x)

    event_list_order_by_date = Event.objects.all().order_by('date')
    event_list = []

    for date in days_in_date_list:
        y = 0
        for event in event_list_order_by_date:
            if(y < event_count):
                if(event.date.day == date):  # is this event's date = today's date?
                    event_list.append(event)
                else:
                    y = y + 1
                    if(y == event_count):
                        event_list.append('None')

    foobar = zip(days_in_date_list, event_list)

    context = {
        'all_events': all_events,
        'event_count': event_count,
        'days': days,
        'date_list': date_list,
        'foobar': foobar,
        'current_month_str': current_month_str,
        'current_month': current_month,
        'current_year': current_year
    }
    return render(request, 'events/index.html', context)


class EventDetailView(DetailView):
    template_name = 'events/details.html'
    context_object_name = 'event'
    queryset = Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        return context

    def get_slug_field(self):
        slug = super(EventDetailView, self).get_slug_field()
        return slug
