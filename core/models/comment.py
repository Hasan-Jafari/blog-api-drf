from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

from .base import BaseModel
from .post import Post



class Comment(BaseModel):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_com'
    )
    content = models.TextField()
    approved = models.BooleanField(default=True)