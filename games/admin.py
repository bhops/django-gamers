from django.contrib import admin
from .models import Game, OwnedGame, Platform

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(OwnedGame)
