from django.db import models


'''optional function to try'''
import re

def getNormalized(url):
    return re.sub('https://www.youtube.com/watch?v=', url)
'''end function'''

class urlInput(models.Model):
    web_url = models.URLField(unique = True

    def __unicode__(self):
        return self.web_url.replace('https://www.youtube.com/watch?v=', '')