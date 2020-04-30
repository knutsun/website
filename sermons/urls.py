from django.urls import path

from . import views

app_name = 'sermons'

urlpatterns = [
    # /sermons/
    path('', views.index, name='index'),
    # /sermons/1 where number is id
    path('<int:pk>/', views.SermonDetailView.as_view(), name='detail'),
]
