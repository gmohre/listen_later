from django.db import models

class Audio(models.Model):
    source_url = models.CharField(max_length=500)
    page_title = models.CharField(max_length=500)
    clip_title = models.CharField(max_length=500)
    date_time = models.DateTimeField(auto_now=True)
    listened = models.BooleanField(default=False)