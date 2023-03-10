from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='url', unique=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='url', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):\
        return reverse('cats', kwargs={'cat_slug': self.slug})
