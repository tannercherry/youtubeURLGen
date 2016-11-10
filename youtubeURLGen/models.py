from django.db import models

class urlInput(models.Model):
    web_url = models.URLField(max_length = 43, unique = True)

    def __unicode__(self):
        return self.web_url