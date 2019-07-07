from .models import Sermons
from django.forms import ModelForm


class SermonForm(ModelForm):
    class Meta:
        model = Sermons
        fields = ['title', 'date', 'description', 'file']
