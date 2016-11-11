from django.shortcuts import render
from youtubegen.forms import urlForm
from .models import urlInput

def input(request):
    form = urlForm(request.POST)
    if request.method == "POST" and form.is_valid():
        tform = form.save(commit = False)
        web = tform.web_url
        web_string = web[33:]
        form.web_url = web_string
        form.save()
    return render(request, 'urlInput/index.html', {'form': form})

def urls(request):
    urlAddresses = list(urlInput.objects.all().values_list())
    return render(request, 'urlInput/urls.html', {'urlAddresses' : urlAddresses})