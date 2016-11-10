from django.shortcuts import render
from youtubegen.forms import urlForm
from .models import urlInput

def input(request):
    form = urlForm()
    if request.POST:
        form = urlForm(request.POST)
        if form.is_valid():
          form.save()

    return render(request, 'urlInput/index.html', {'form': form})

def urls(request):
    urlAddresses = urlInput.objects.all().values_list()

    return render(request, 'urlInput/urls.html', {'url_list' : urlAddresses})