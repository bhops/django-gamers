from django.db import models
from django.contrib.auth.models import User
from games.models import OwnedGame

class LookingForPost(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(OwnedGame)

    def __str__(self):
        return self.user.username + ' - ' + self.game.game.title

    class Meta:
        ordering = ('user',)


