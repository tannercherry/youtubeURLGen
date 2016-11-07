from django.shortcuts import render
from django.http import HttpResponseRedirect

from youtubegen.forms import urlForm
from .models import urlInput
from django.views import generic

def input(request):
    form = urlForm()
    return render(request, 'urlInput/index.html', {'form': form})

class urls(generic):
    template_name = 'urlInput.urls.html'
    def get_queryset(web_url):
        return urlInput.objects.all()