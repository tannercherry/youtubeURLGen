from django.db import models

from urllib.parse import urlparse

def url_web(value):
    query = urlparse(value)
    return query.path[33:]

class urlInput(models.Model):
    web_url = models.URLField(unique = True)

    def __unicode__(self):
        return self.web_url