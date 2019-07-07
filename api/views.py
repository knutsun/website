from .serializers import EventSerializer, SermonSerializer
from rest_framework import generics
from sermons.models import Sermons
from events.models import Event


class EventApiView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailApiView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SermonApiView(generics.ListAPIView):
    queryset = Sermons.objects.all()
    serializer_class = SermonSerializer


class SermonDetailApiView(generics.RetrieveAPIView):
    queryset = Sermons.objects.all()
    serializer_class = SermonSerializer
