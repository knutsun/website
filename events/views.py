from django.shortcuts import render
from .models import Event
import calendar
import datetime
from django.utils.formats import date_format
from django.views.generic import ListView, DetailView, FormView
import itertools


def index(request):
    cal = calendar.Calendar()
    days = cal.itermonthdays2(2018, 11)
    all_events = Event.objects.all()
    event_count = Event.objects.all().count()

    date_list = []
    days_in_date_list = []

    for day in days:
        date_list.append(day)

    for x, y in date_list:
        days_in_date_list.append(x)

    event_list_order_by_date = Event.objects.all().order_by('date')
    event_list = []
    x = 0
    for date in days_in_date_list:
        if(x < event_count):
            if(event_list_order_by_date[x].date.day == date):
                event_list.append(event_list_order_by_date[x])
                x = x + 1
            else:
                event_list.append('None')

    foobar = zip(days_in_date_list, event_list)

    context = {
    'all_events': all_events,
    'days': days,
    'date_list':date_list,
    'foobar': foobar,
    }
    return render(request, 'events/index.html', context)
