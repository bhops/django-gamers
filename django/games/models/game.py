from django.db import models
from django.template.defaultfilters import slugify
from .platform import Platform

class Game(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(null=True)
    gr_url = models.URLField(null=True)
    publisher = models.CharField(null=True, max_length=150)
    released = models.DateField(null=True)
    rating = models.CharField(max_length=10, null=True)
    added = models.DateField(auto_now_add=True)
    platform = models.ForeignKey(Platform, related_name='games')

    def __str__(self):
        return '[' + self.platform.name + '] ' + self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, create a slug.
            self.slug = self.platform.slug+'-'+slugify(self.title)
        super(Game, self).save(*args, **kwargs)

    class Meta:
        ordering = ('title',)
