from django.db import models
from django.db.models.signals import pre_save
from  abc

class Platform(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    released = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    released = models.DateTimeField()
    added = models.DateField(auto_now_add=True)
    platform = models.ForeignKey(Platform, related_name='games')

    def __str__(self):
        return self.title + ' (' + self.platform.name + ')'

    class Meta:
        ordering = ('title',)
