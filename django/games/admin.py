from django.contrib import admin
from .models import Game, Platform

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'publisher', 'rating', 'gr_url')
    list_filter = (
        ('platform', admin.RelatedOnlyFieldListFilter),
        ('publisher'),
    )

admin.site.register(Game, GameAdmin)
admin.site.register(Platform)
