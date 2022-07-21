from django.db import models

# Create your models here.

class Image(models.Model):
    ImgName = models.CharField(max_length=50, blank=False)
    ImgURL = models.URLField(blank=False, max_length=1000)
    ImgDetails = models.TextField(default=None, max_length=1500, blank=False)

    