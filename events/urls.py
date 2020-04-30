from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    # /events/
    path('', views.index, name='index'),
    # /events/1 where number is id
    # path('<int:pk>/', views.EventDetailView.as_view(), name='detail'),
    path('<int:year>/<int:month>/<int:day>/<int:pk>',
         views.EventDetailView.as_view(), name='detail'),
]
