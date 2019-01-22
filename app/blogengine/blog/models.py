from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time
from .utils import ObjectMixin
from transliterate import translit



class Post(ObjectMixin, models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add = True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    details_url = 'post_details_url'
    update_url = 'post_update_url'
    delete_url = 'post_delete_url'

    class Meta:
        ordering = ['-date_pub']


class Tag(ObjectMixin, models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    details_url = 'tag_details_url'
    update_url = 'tag_update_url'
    delete_url = 'tag_delete_url'

    class Meta:
        ordering = ['title']
