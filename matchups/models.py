from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from games.models import Game

class LookingForPost(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    active = models.BooleanField(default=True)
    filled = models.BooleanField(default=False)
    description = models.TextField(default='')

    def __str__(self):
        return self.user.username + ' - ' + self.game.game.title

    class Meta:
        ordering = ('user',)

class Schedule(models.Model):
    """
    This model is used to create a link between a User and many ScheduleBlocks.
    """
    user = models.OneToOneField(User)

    def __str__(self):
        return '[Schedule] ' + self.user.username

class ScheduleBlock(models.Model):
    """
    This model represents a block of time on a particular day in which a user
    is available to play games.
    """
    MONDAY = 'M'
    TUESDAY = 'T'
    WEDNESDAY = 'W'
    THURSDAY = 'Th'
    FRIDAY = 'F'
    SATURDAY = 'Sa'
    SUNDAY = 'Su'
    DAY_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday')
    )
    day_of_week = models.CharField(max_length=2, choices=DAY_CHOICES, default=MONDAY)
    time_from = models.TimeField(default='00:00')
    time_to = models.TimeField(default='23:59')
    schedule = models.ForeignKey(Schedule, related_name='blocks')
    # For now, we don't want a user to have multiple schedules on the same day.
    # In the future, someone SHOULD be able to have multiple schedule blocks
    # on the same day. If they overlap, we should then merge them.
    unique_together = (('day_of_week', 'schedule'),)

    def __str__(self):
        return '[' + self.day_of_week + '] ' + str(self.time_from) + ' - ' + str(self.time_to)

    def clean(self):
        if self.time_from >= self.time_to:
            raise ValidationError('time_from (%s) must be earlier than time_to(%s)' %
                                (self.time_from, self.time_to))


