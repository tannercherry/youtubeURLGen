from django import forms
from django.forms import ModelForm

from youtubeURLGen.models import urlInput

class urlForm(ModelForm):
    class Meta:
        model = urlInput

        fields = ['web_url']
