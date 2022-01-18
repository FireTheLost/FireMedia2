import datetime

from django.db import models
from django.urls import reverse

import uuid


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='The Random ID For The Blog Post')

    title = models.CharField(max_length=256)
    description = models.CharField(max_length=64)
    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    body = models.TextField(max_length=65536, help_text='The Main Body Of The Blog Post')
    published = models.DateTimeField(default=datetime.datetime.now())

    visibility = models.CharField(max_length=16, default="Public")

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog-post', args=[str(self.id)])


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='The Random ID For The User')

    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    username = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.username}'
