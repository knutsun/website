from .forms import ContactForm
from .models import Contact

from django import forms
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import FormView


class index(FormView):

	self.template_name = 'contact/index.html'
	self.form_class = ContactForm
	self.success_url = 'contact/index.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None) # context is None; blank form data
		return render(request, self.template_name, {'form': form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST) # context is POST

		if form.is_valid():
			form.save()
			messages.success(request, "Message successfully sent", extra_tags="message_success")
			return render(request, self.success_url)
		else:
			return render(request, self.template_name, {'form': form})
