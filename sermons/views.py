from django.shortcuts import render
from .models import Sermons
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django import forms
from .forms import SermonForm
from django.contrib import messages
from django.utils.formats import date_format
from django.views.generic import ListView, DetailView, FormView
from django.utils.decorators import method_decorator

def index(request):
	all_sermons = Sermons.objects.all()
	sermon_count = Sermons.objects.all().count()
	search_term = ""
	search_result_count = ""
	if 'search' in request.GET:
		search_term = request.GET['search']
		all_sermons = all_sermons.filter(
			Q(description__icontains=search_term) |
			Q(title__icontains=search_term)
		)
		search_result_count = all_sermons.filter(
			Q(description__icontains=search_term) | Q(title__icontains=search_term)).count()
		if search_result_count == 1:
			search_result_count = str(search_result_count) + " result"
		elif search_result_count == 0:
			messages.success(request, "Your search yielded no results.", extra_tags="message_failure")
			all_sermons = Sermons.objects.all()
		else:
			search_result_count = str(search_result_count) + " results"
	context = {
		'all_sermons': all_sermons,
		'search_term': search_term,
		'search_result_count': search_result_count,
		'sermon_count': sermon_count

	}
	return render(request, 'sermons/index.html', context)

class SermonDetailView(DetailView):
	template_name = 'sermons/details.html'
	context_object_name = 'sermon'
	queryset = Sermons.objects.all()

	def get_context_data(self, **kwargs):
		context = super(SermonDetailView, self).get_context_data(**kwargs)
		return context