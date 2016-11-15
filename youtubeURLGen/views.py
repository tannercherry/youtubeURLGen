from django.shortcuts import render, HttpResponseRedirect
from youtubegen.forms import urlForm
from .models import urlInput

def input(request):
    form = urlForm(request.POST)
    if form.is_valid():
        extra_form = form.save(commit = False)
        web = extra_form.web_url
        if web.startswith("https://www.youtube.com/watch?v="):
            web_string = web.replace("https://www.youtube.com/watch?v=", "")
            new_input = urlInput(web_url=web_string)
            new_input.validate_unique()
            new_input.save()
        elif web.startswith("www.youtube.com/watch?v="):
            web_string = web.replace("www.youtube.com/watch?v=", "")
            new_input = urlInput(web_url=web_string)
            new_input.validate_unique()
            new_input.save()
        elif web.startswith("http://www.youtube.com/watch?v="):
            web_string = web.replace("http://www.youtube.com/watch?v=", "")
            new_input = urlInput(web_url=web_string)
            new_input.validate_unique()
            new_input.save()
        elif web.startswith("https://youtube.com/watch?v="):
            web_string = web.replace("https://youtube.com/watch?v=", "")
            new_input = urlInput(web_url=web_string)
            new_input.validate_unique()
            new_input.save()
        elif web.startswith("youtube.com/watch?v="):
            web_string = web.replace("youtube.com/watch?v=", "")
            new_input = urlInput(web_url=web_string)
            new_input.validate_unique()
            new_input.save()
        else:
            return HttpResponseRedirect("/error.html")
    return render(request, 'urlInput/index.html', {'form': form})

def urls(request):
    urlAddresses = list(urlInput.objects.all().values_list())
    return render(request, 'urlInput/urls.html', {'urlAddresses' : urlAddresses})