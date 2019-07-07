from .views import EventApiView, EventDetailApiView, SermonApiView, SermonDetailApiView
from django.urls import path

urlpatterns = [

    # Sermon endpoints
    path('sermons', SermonApiView.as_view()),
    path('sermons/<int:pk>/', SermonDetailApiView.as_view()),


    # Event endpoints
    path('events', EventApiView.as_view()),
    path('events/<int:pk>/', EventDetailApiView.as_view()),

]
