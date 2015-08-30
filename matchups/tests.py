from django.test import TestCase
from django.contrib.auth.models import User
from .models import Schedule, ScheduleBlock

class ScheduleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testing123'
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_string_representation(self):
        """
        Verify that the string representation of Schedule is correct.
        """
        s = Schedule(user=self.user)
        self.assertEqual(str(s), '[Schedule] testuser')

    def test_verbose_name_plural(self):
        """
        Verify that plural of `schedule` is `schedules`.
        """
        self.assertEqual(str(Schedule._meta.verbose_name_plural), "schedules")

    def test_back_relation(self):
        """
        Verify that <user>.schedule returns the user's schedule.
        """
        s = Schedule(user=self.user)
        self.assertEqual(str(self.user.schedule), str(s))


class ScheduleBlockTest(TestCase):
    def setUp(self):
        ScheduleTest.setUp(self)
        self.schedule = Schedule(user=self.user)
        self.schedule.save()

    def tearDown(self):
        self.schedule.delete()
        ScheduleTest.tearDown(self)

    def test_string_representation(self):
        """
        Verify that the string representation of a ScheduleBlock is correct.
        """
        sb = ScheduleBlock(schedule=self.schedule)
        self.assertEqual(str(sb), '[M] 00:00 - 23:59')

    def test_verbose_name_plural(self):
        """
        Verify that the plural of 'schedule block' is 'schedule blocks'.
        """
        self.assertEqual(str(ScheduleBlock._meta.verbose_name_plural), "schedule blocks")

    def test_back_relation(self):
        """
        Verify that <schedule>.scheduleblocks returns the ScheduleBlocks.
        """
        self.sb1 = ScheduleBlock(schedule=self.schedule)
        self.sb2 = ScheduleBlock(schedule=self.schedule, day_of_week='F')
        self.sb1.save()
        self.sb2.save()
        self.assertEqual(len(self.schedule.blocks.all()), 2)
        self.sb1.delete()
        self.sb2.delete()

    def test_invalid_time(self):
        # Find a way for this to work
        pass
        #sb = ScheduleBlock(schedule=self.schedule,
        #                   time_from="01:00",
        #                   time_to="00:59")
