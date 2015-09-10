from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import UserProfile

def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        profile = UserProfile(user=user)
        profile.save()

post_save.connect(create_profile, sender=User)
