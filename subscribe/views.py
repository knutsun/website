from django.core.mail import send_mail
from django.shortcuts import render
from gway.settings import EMAIL_HOST_USER
from . import forms


def subscribe(request):

    sub = forms.Subscribe()

    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Gateway Baptist Church'

        message = 'Hello! Welcome to Gateway Baptist Church! \
        We are happy to have you as a subscriber.'

        recipient = str(sub['Email'].value())

        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)

        return render(request, 'subscribe/success.html', {'recipient': recipient})
    return render(request, 'subscribe/index.html', {'form': sub})
