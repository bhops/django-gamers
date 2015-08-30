from django.contrib import admin
from .models import Game, Platform

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Game)
admin.site.register(Platform)
