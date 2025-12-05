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
            slug = slugify(self.title, allow_unicode=True)
            slugy = slug
            slug_num = 1
            while Tag.objects.filter(slug=slug).exists():
                slug = f'{slugy}-{slug_num}'
                slug_num += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title