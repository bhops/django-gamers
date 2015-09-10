from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    PNTD = '?'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (PNTD, 'Prefer not to disclose'),
    )
    user = models.OneToOneField(User, related_name="profile")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(null=True)
    sex = models.CharField(max_length=1,
                           choices=SEX_CHOICES,
                           default=PNTD)
    about = models.CharField(max_length=255, default='This user hasn\'t updated their profile.')

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'users'
        ordering = ('user',)
