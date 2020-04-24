from django.shortcuts import render
from events.models import Event
from django.core.mail import send_mail
from django.shortcuts import render

from gway.settings import EMAIL_HOST_USER
from subscribe import forms
from subscribe.models import Subscribers

import random


def index(request):

    all_events = Event.objects.all()
    event_count = all_events.count()
    three_events = all_events.order_by('-date')[:3]
    sub = forms.Subscribe()

    context = {
        'all_events': all_events,
        'event_count': event_count,
        'three_events': three_events,
        'form': sub,
    }

    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to the Gateway Newsletter'
        message = 'We are happy you\'ve subscribed.'
        recipient = str(sub['Email'].value())

        Subscribers.objects.create(email=recipient, conf_num=random_digits())

        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)

        recipient_list = Subscribers.objects.all()

        return render(request, 'subscribe/success.html', {'recipient': recipient,
                                                          'recipient_list': recipient_list})

    return render(request, 'index.html', context)


def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)
