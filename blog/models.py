from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=150)
    active = models.BooleanField(verbose_name=_('active'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


POST_STATUS = [
    ('draft', _('Draft')),
    ('published', _('Published')),
]


class Post(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    lead = models.CharField(verbose_name=_('lead'), max_length=1024, null=True, blank=True)
    body = models.TextField(verbose_name=_('body'), )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    thumbnail = models.ImageField(verbose_name=_('thumbnail'), upload_to='thumbnails', default='thumbnail.png')
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('updated'), auto_now=True)
    status = models.CharField(verbose_name=_('status'), max_length=15, choices=POST_STATUS, default='draft')
    featured = models.BooleanField(verbose_name=_('featured'), null=True, default=False)
    publish_time = models.DateTimeField(verbose_name=_('publish time'), null=True, blank=True)
    slug = models.SlugField(verbose_name=_('slug'), allow_unicode=True, null=False, unique_for_date='publish_time')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-publish_time']
