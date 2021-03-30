from django.db import models

#NOTE: Skipping id field, as django adds an id field by default

class Song(models.Model):
    name = models.CharField(max_length=100)
    duration_in_secs = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField()

class Podcast(models.Model):
    name = models.CharField(max_length=100)
    duration_in_secs = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField()
    host = models.CharField(max_length=100)
    participants = models.JSONField()

class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration_in_secs = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField()
