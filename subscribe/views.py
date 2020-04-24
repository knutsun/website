from django.shortcuts import render

from .models import Subscribers
from django.contrib.auth.decorators import login_required


@login_required
def subscribers(request):

    recipient_list = Subscribers.objects.all()

    return render(request, 'subscribe/subscribers.html', {'recipient_list': recipient_list})
