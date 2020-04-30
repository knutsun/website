from django.forms import ModelForm

from .models import Sermons


class SermonForm(ModelForm):
    class Meta:
        model = Sermons
        fields = ['title', 'date', 'description', 'file']
