from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_updete = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женшины'
        verbose_name_plural = 'Известные женшины'
        ordering = ['-time_create', 'title']


class Coment(models.Model):
    name = models.CharField(max_length=150, blank=True, verbose_name='Имя')
    email = models.CharField(max_length=150, blank=True, verbose_name='Ваш email')
    text = models.TextField(max_length=400, verbose_name='Текс комментария')

    class Meta:
        ordering = ['-id']






