from django.db import models

class urlInput(models.Model):
    web_url = models.URLField(range(33-43), unique = True)

    def __unicode__(self):
        return self.web_url