from django.db import models
from django import forms
from django.forms import ModelForm

class Sermons(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField()
	description = models.TextField()
	file = models.FileField(max_length=1000)

	class Meta:
		permissions = (
				('can_submit', "Can submit a new Sermon"),
			)


	def __str__(self):
		return self.title
