from django.shortcuts import render
from youtubegen.forms import urlForm

from .models import urlInput

def input(request):
    form = urlForm()

    if request.POST:
        form = urlForm(request.POST)
        if form.is_valid():
          urlAdd = form.save()

    return render(request, 'urlInput/index.html', {'form': form})

def urls(request):
    urlAddresses = urlInput.objects.all().values()
    return render(request, 'urlInput/urls.html', {'urlAddresses' : urlAddresses})