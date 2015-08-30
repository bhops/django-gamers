from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile
from games.models import OwnedGame

class UserProfileAdmin(admin.StackedInline):
    model = UserProfile
    # We only want 1 user profile per user
    extra = 0
    min_num = 1
    max_num = 1
    can_delete = False
    inline_classes = ('collapse open',) # default to expanded
    verbose_name = 'Profile'
    verbose_name_plural = 'Profile'

class OwnedGamesAdmin(admin.StackedInline):
    model = OwnedGame
    extra = 0 # Don't show extra blanks in Admin

class UserAdmin(admin.ModelAdmin):
    ordering = ('username',)
    fields = ('username', 'email', 'first_name', 'last_name', 'password',
              'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',
              'date_joined')
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_superuser', 'is_staff')
    inlines = [ UserProfileAdmin, OwnedGamesAdmin ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
