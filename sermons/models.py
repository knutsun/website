import audioread

from django.db import models


class Sermons(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    file = models.FileField(max_length=1000)

    class Meta:
        permissions = (
                ('can_submit', "Can submit a new Sermon"),
            )
        verbose_name = 'Sermon'

    def __str__(self):
        return self.title

    def get_duration(self):
        f = audioread.audio_open(self.file.path)
        duration = round(f.duration/60)
        return duration
