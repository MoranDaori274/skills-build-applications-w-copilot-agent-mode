from djongo import models

class User(models.Model):
	_id = models.ObjectIdField()
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=100)
	team = models.CharField(max_length=50)
	def __str__(self):
		return self.email

class Team(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=50, unique=True)
	description = models.TextField(blank=True)
	def __str__(self):
		return self.name

class Activity(models.Model):
	_id = models.ObjectIdField()
	user = models.CharField(max_length=100)
	type = models.CharField(max_length=50)
	duration = models.IntegerField()  # in minutes
	date = models.DateField()
	def __str__(self):
		return f"{self.user} - {self.type}"

class Leaderboard(models.Model):
	_id = models.ObjectIdField()
	team = models.CharField(max_length=50)
	points = models.IntegerField()
	def __str__(self):
		return f"{self.team}: {self.points}"

class Workout(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=100)
	description = models.TextField()
	difficulty = models.CharField(max_length=20)
	def __str__(self):
		return self.name
