from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
import requests

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

class Game(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    released = models.DateField(auto_now_add=True)
    added = models.DateField(auto_now_add=True)
    platform = models.ForeignKey(Platform, related_name='games')

    def __str__(self):
        return '[' + self.platform.name + '] ' + self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, create a slug.
            self.slug = slugify(self.title)
        super(Game, self).save(*args, **kwargs)

    class Meta:
        ordering = ('title',)

@receiver(pre_save, sender=Game)
def get_game_details(sender, **kwargs):
    instance = kwargs.get('instance', None)
    if instance is not None and instance.description == 'tbd':
        url = 'https://metacritic-2.p.mashape.com/find/game?platform='+instance.platform.name.lower()+'&title='+instance.title
        headers = {'X-Mashape-Key': 'VR9AsO5oummsh0k12JNdlbnzAzj0p1s152ejsnyjkKlJ2U5hI3', 'Accept': 'application/json'}
        r = requests.get(url, headers=headers)
        json = r.json()
        result = json.get('result', None)
        instance.description = result.get('summary', 'No Description Available') if result else 'No Description Available'
