from events.models import Event
from sermons.models import Sermons
from .serializers import EventSerializer, SermonSerializer
from rest_framework import viewsets


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermons.objects.all()
    serializer_class = SermonSerializer
