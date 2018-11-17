from django.shortcuts import render
from .models import Contact
from django import forms
from .forms import ContactForm
from django.contrib import messages
from django.utils.formats import date_format
from django.views.generic import ListView, DetailView, FormView


class index(FormView):

	template_name = 'contact/index.html'
	form_class = ContactForm
	success_url = 'contact/index.html'

	#display blank form
	def get(self, request):
		form = self.form_class(None) #context is None; blank form data
		return render(request, self.template_name, {'form': form})

	#process form data
	def post(self, request):
		form = self.form_class(request.POST, request.FILES) #context is POST

		if form.is_valid():
			form.save()
			messages.success(request, "Message successfully sent", extra_tags="message_success")
			return render(request, self.success_url)
		else:
			return render(request, self.template_name, {'form': form})
