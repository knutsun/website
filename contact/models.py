from django.db import models


class Contact(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    name = models.CharField(max_length=35)
    email = models.EmailField(max_length=70, default="None")

    def __str__(self):
        return self.name + " - " + self.subject
