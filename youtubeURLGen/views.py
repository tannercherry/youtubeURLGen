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
    urlAddresses = urlInput.objects.all().values_list()
    return render(request, 'urlInput/urls.html', {'urlAddresses' : urlAddresses})


'''.raw("SELECT substring(web_url, LEN(web_url) - PATINDEX('=', web_url)) FROM db")'''