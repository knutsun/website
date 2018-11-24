from django.shortcuts import render
from events.models import Event
import calendar
import datetime
from django.utils.formats import date_format
from django.views.generic import ListView, DetailView, FormView

def index(request):
    # cal = calendar.Calendar()
    # days = cal.itermonthdays2(2018, 11)
    all_events = Event.objects.all()
    event_count = Event.objects.all().count()
    three_events = Event.objects.all().order_by('date')[:3]

    context = {
    'all_events': all_events,
    'event_count': event_count,
    'three_events': three_events,
    }
    return render(request, 'index.html', context)
