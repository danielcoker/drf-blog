from django.db import models

from authentication.models import User
from base.models import TimestampedModel


class PostQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Post(TimestampedModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    image = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title
