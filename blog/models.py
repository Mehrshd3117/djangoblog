from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.conf import settings


class Category(models.Model):
    title = models.CharField(verbose_name=_('category'), max_length=255)
    active = models.BooleanField(verbose_name=_('active'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name=_('parent'))
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True, verbose_name=_('slug'))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('updated'))

    def save(
            self,
            *args,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.slug = slugify(self.title)
        super(Category, self).save()

    def str(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = _('draft'),
        PUBLISHED = _('published')

    title = models.CharField(verbose_name=_('title'), max_length=255)
    slug = models.SlugField(verbose_name=_('slug'), allow_unicode=True, unique=True, null=True, blank=True,
                            unique_for_date='publish_time')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'))
    lead = models.CharField(verbose_name=_('lead'), max_length=1024, null=True, blank=True)
    body = models.TextField(verbose_name=_('body'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('updated'), auto_now=True)

    status = models.CharField(verbose_name=_('status'), max_length=15, choices=StatusChoices.choices,
                              default=StatusChoices.DRAFT)
    publish_time = models.DateTimeField(verbose_name=_('publish_time'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-publish_time']
