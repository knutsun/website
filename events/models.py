from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    short_description = models.TextField()
    long_description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name
