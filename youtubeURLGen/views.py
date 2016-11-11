from django.shortcuts import render
from youtubegen.forms import urlForm
from .models import urlInput

import re

def clean_web_url(self):
    web = self.data['web_url']
    web_string = re.sub("https://www.youtube.com/watch?v=", "", web)
    return web_string

def input(request):
    form = urlForm(request.POST)
    if request.method == "POST" and form.is_valid():
        form.save(id)
        form.web_url = clean_web_url(form)
        form.save('web_url')

    return render(request, 'urlInput/index.html', {'form': form})

def urls(request):
    urlAddresses = list(urlInput.objects.all().values_list())
    return render(request, 'urlInput/urls.html', {'urlAddresses' : urlAddresses})