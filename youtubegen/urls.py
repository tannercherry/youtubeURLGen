from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^input/', include ('youtubeURLGen.urls')),
    url(r'^admin/', admin.site.urls)
]
