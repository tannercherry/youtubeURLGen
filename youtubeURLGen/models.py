from django.db import models



'''optional function to try'''
import re

def getNormalized(url):
    url = url.replace('https://www.youtube.com/watch?v=', '')
    return url

'''end function'''

class urlInput(models.Model):
    web_url = models.URLField(max_length = 43, unique = True)
    getNormalized(web_url)

    def __unicode__(self):
        return self.web_url