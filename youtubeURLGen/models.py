from django.db import models

class urlInput(models.Model):
    web_url = models.CharField(max_length = 43, unique = True)

    def __str__(self):
        return self.web_url