# Create your models here.
from django.db import models
from django.urls import reverse


class Blogpost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        print(self.slug)
        return reverse('view_blog_post', args=[self.slug])
