from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    # /events/
    path('', views.index, name='index'),
]
