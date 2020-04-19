from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import FormView
from django.conf import settings

import certifi
import json
import urllib


class index(FormView):

    form_class = ContactForm
    template_name = 'contact/index.html'
    success_url = 'contact/index.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)  # context is None; blank form data
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)  # context is POST

        if form.is_valid():

            # get the token submitted in the form
            recaptcha_response = self.request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            cert_path = certifi.where()

            payload = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(payload).encode()
            req = urllib.request.Request(url, data=data)

            # verify the token submitted with the form is valid
            response = urllib.request.urlopen(req, cafile=cert_path)
            result = json.loads(response.read().decode())

            if (not result['success']):
                messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
                return super().form_invalid(form)

            form.save()
            messages.success(request, "Message successfully sent",
                                      extra_tags="message_success")
            return render(request, self.success_url, {'sitekey': settings.GOOGLE_RECAPTCHA_SITE_KEY})
        else:
            return render(request, self.template_name, {'form': form, 'sitekey': settings.GOOGLE_RECAPTCHA_SITE_KEY})
