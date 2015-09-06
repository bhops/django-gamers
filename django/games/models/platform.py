from django.db import models
from django.template.defaultfilters import slugify

class Platform(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, create a slug.
            self.slug = slugify(self.name)
        super(Platform, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)


