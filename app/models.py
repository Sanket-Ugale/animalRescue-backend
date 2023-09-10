# In models.py
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name
