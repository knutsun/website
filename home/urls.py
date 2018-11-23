from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
	# /events/
    path('', views.index, name='index'),
]
