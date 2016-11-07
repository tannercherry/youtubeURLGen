from django.conf.urls import url

from . import views

app_name = 'youtubeURLGen'
urlpatterns = [
    url(r'^$', views.input, name='input'),
    url(r'^urls/', views.urls, name='urls')
]