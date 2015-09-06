from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    PNTD = '?'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (PNTD, 'Prefer not to disclose'),
    )
    user = models.OneToOneField(User)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    dob = models.DateField()
    sex = models.CharField(max_length=1,
                           choices=SEX_CHOICES,
                           default=MALE)
    about = models.CharField(max_length=255, default='This user hasn\'t updated their profile.')

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('user',)
