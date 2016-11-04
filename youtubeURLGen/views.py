from django.shortcuts import render
from django.http import HttpResponseRedirect

from youtubegen.forms import urlForm

def input(request):
    form = urlForm()
    return render(request, 'urlInput/index.html', {'form': form})