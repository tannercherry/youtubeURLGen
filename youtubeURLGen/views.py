from django.shortcuts import render
from youtubegen.forms import urlForm
from .models import urlInput

def input(request):
    form = urlForm(request.POST)
    if request.method == "POST" and form.is_valid():
        form.save(id)
        web = form.data['web_url']
        web_string = web[33:]
        form.web_url = web_string
        '''find way to save string as form here'''
    return render(request, 'urlInput/index.html', {'form': form})

def urls(request):
    urlAddresses = list(urlInput.objects.all().values_list())
    return render(request, 'urlInput/urls.html', {'urlAddresses' : urlAddresses})