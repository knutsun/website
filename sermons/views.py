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
import audioread


def index(request):
	sermon_objs = Sermons.objects
	all_sermons = sermon_objs.all()
	sermon_count = all_sermons.count()
	sermons_ordered_by_date = sermon_objs.order_by('date')

	search_text = None
	search_result_count = None

	if 'search' in request.GET:
		search_text = request.GET['search']
		all_sermons = all_sermons.filter(
			Q(description__icontains=search_text) |
			Q(title__icontains=search_text)
		)
		search_result_count = all_sermons.count()

		if search_result_count:
			if search_result_count > 1:
				search_result_count = '{} results.'.format(search_result_count)
			else:
				search_result_count = '{} result.'.format(search_result_count)
		else:
			messages.success(request, "Your search yielded no results.", extra_tags="message_failure")
			all_sermons = Sermons.objects.all()


	context = {
		'all_sermons': all_sermons,
		'first_sermon': sermons_ordered_by_date[0],
		'last_sermon': sermons_ordered_by_date[sermon_count-1],
		'search_text': search_text,
		'search_result_count': search_result_count,
		'sermon_count': sermon_count,
	}
	
	return render(request, 'sermons/index.html', context)


class SermonDetailView(DetailView):
	template_name = 'sermons/details.html'
	context_object_name = 'sermon'
	queryset = Sermons.objects.all()

	def get_context_data(self, **kwargs):
		context = super(SermonDetailView, self).get_context_data(**kwargs)
		return context
