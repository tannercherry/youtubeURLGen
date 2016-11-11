from django.shortcuts import render
from youtubegen.forms import urlForm
from .models import urlInput

def input(request):
    form = urlForm(request.POST)
    if form.is_valid():
        extra_form = form.save(commit = False)
        web = extra_form.web_url
        web_string = web.replace("https://www.youtube.com/watch?v=", "")
        new_input = urlInput(web_url=web_string)
        new_input.validate_unique()
        new_input.save()
    return render(request, 'urlInput/index.html', {'form': form})

def urls(request):
    urlAddresses = list(urlInput.objects.all().values_list())
    return render(request, 'urlInput/urls.html', {'urlAddresses' : urlAddresses})