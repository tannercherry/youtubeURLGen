from django.conf.urls import url

from . import views

app_name = 'youtubeUrLGen'
urlpatterns = [
    url(r'^$', views.input, name='input'),
]