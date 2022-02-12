from django.db import models


# Create your models here.
class Book(models.Model):
    book = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    author = models.CharField(max_length=40, null=False, blank=False)
    published_at = models.DateTimeField(null=True, blank=False)
