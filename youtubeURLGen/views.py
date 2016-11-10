from django.shortcuts import render
from youtubegen.forms import urlForm
from .models import urlInput

from urllib.parse import urlparse

def url(value):
    parsedURL = urlparse(value)
    return parsedURL.argument

def input(request):
    form = urlForm()
    if request.POST:
        form = urlForm(request.POST)
        if form.is_valid():
          form.save()

    return render(request, 'urlInput/index.html', {'form': form})

def urls(request):
    urlAddresses = urlInput.objects.all().values_list()
    url_list = list(urlAddresses)
    a = 0
    num = len(url_list) - 1
    while a >= num:
        if type(url_list[a]) == int:
            a = a + 1
        else:
            url(url_list[a])
            a = a + 1

    return render(request, 'urlInput/urls.html', {'url_list' : url_list})