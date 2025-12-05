from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

from .base import BaseModel
from .category import Category
from .tag import Tag



class Status(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published', 'Published'
    
class Post(BaseModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts'
    )
    categories = models.ManyToManyField(
        Category,
        related_name='posts'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='posts'
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )
    views_count =  models.PositiveIntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
            slug = slugify(self.title, allow_unicode=True)
            slugy = slug
            slug_num = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f'{slugy}-{slug_num}'
                slug_num += 1
            self.slug = slug
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title