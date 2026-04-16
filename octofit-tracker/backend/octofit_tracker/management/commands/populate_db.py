from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team=marvel.name),
            User(email='steve@rogers.com', name='Steve Rogers', team=marvel.name),
            User(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name),
            User(email='clark@kent.com', name='Clark Kent', team=dc.name),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(user='Tony Stark', type='Running', duration=30, date=timezone.now().date()),
            Activity(user='Steve Rogers', type='Cycling', duration=45, date=timezone.now().date()),
            Activity(user='Bruce Wayne', type='Swimming', duration=60, date=timezone.now().date()),
            Activity(user='Clark Kent', type='Flying', duration=120, date=timezone.now().date()),
        ]
        Activity.objects.bulk_create(activities)

        # Workouts
        workouts = [
            Workout(name='Super Strength', description='Strength workout for heroes', difficulty='Hard'),
            Workout(name='Speed Training', description='Speed workout for heroes', difficulty='Medium'),
        ]
        Workout.objects.bulk_create(workouts)

        # Leaderboard
        Leaderboard.objects.create(team=marvel.name, points=100)
        Leaderboard.objects.create(team=dc.name, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
