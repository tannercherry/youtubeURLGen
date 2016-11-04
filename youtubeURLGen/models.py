from django.db import models

class urlInput(models.Model):
    web_url = models.URLField(null=False, blank=False)
