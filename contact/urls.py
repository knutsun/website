from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    # /contact/
    path('', views.index.as_view(), name='index'),

]
