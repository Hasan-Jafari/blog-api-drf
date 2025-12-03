from django.db import models
from slugify import slugify

from .base import BaseModel



class Tag(BaseModel):
    title = models.CharField(
        max_length=50,
        unique=True
    )
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title