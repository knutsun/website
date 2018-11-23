
from django.urls import path, include
from . import views

app_name = 'events'

urlpatterns = [
	# /events/
    path('', views.index, name='index'),
]
