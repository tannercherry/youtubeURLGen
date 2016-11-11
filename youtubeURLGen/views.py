from django.shortcuts import render
from youtubegen.forms import urlForm
from .models import urlInput
from urllib.parse import urlparse

def input(request):
    form = urlForm()
    if request.POST:
        form = urlForm(request.POST)
        if form.is_valid():
          form.save()

    return render(request, 'urlInput/index.html', {'form': form})

def update(request, ID):
    a = 0
    for a in urlInput.objects.ID():
        change_url = urlInput.objects.get(ID=a)
        change_url = change_url[33:]
        change_url.save()

def urls(request):
    urlAddresses = urlInput.objects.all().values_list()
    return render(request, 'urlInput/urls.html', {'url_list' : urlAddresses})