from django.db import models

class Link(models.Model):
    short_link = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
