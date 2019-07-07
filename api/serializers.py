from rest_framework import serializers
from sermons.models import Sermons
from events.models import Event

class SermonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sermons
		fields = ('id', 'title', 'date', 'description', 'file')

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ('id', 'name', 'date', 'short_description', 
			'long_description', 'start_time', 'end_time')
