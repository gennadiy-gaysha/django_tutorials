from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add thumbnail later
    thumbs = models.ImageField(default='default.png', blank=True)
    # add in author later

    def __str__(self):
        return f'{self.title}'

    def snippet(self):
        return f'{self.body[:70]} [read more...]'