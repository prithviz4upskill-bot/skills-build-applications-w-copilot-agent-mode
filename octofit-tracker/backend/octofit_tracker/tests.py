from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC Superheroes')
        user = User.objects.create(email='batman@dc.com', username='Batman', team=team, is_superhero=True)
        self.assertEqual(str(user), 'Batman')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        user = User.objects.create(email='spiderman@marvel.com', username='Spiderman', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, date='2025-12-29')
        self.assertEqual(str(activity), 'Spiderman - Running')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        user = User.objects.create(email='ironman@marvel.com', username='Ironman', team=team, is_superhero=True)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(str(leaderboard), 'Ironman - 100')
