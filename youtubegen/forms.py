from django import forms

class urlForm(forms.Form):
    youtube_url = forms.URLField(label = 'Copy and Paste Here')
