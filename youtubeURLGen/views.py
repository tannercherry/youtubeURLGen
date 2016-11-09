from django.shortcuts import render
from youtubegen.forms import urlForm

from .models import urlInput

import re

def getNormalized(url):
    return re.sub(r'https://youtube.com/watch?v=', r'', url)

def input(request):
    form = urlForm()

    if request.POST:
        form = urlForm(request.POST)
        if form.is_valid():
          '''form = str(form)'''
          '''getNormalized(form)'''
          form.save()

    return render(request, 'urlInput/index.html', {'form': form})

def urls(request):
    urlAddresses = urlInput.objects.all().values_list()
    return render(request, 'urlInput/urls.html', {'urlAddresses' : urlAddresses})