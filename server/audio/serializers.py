import pytz
from datetime import datetime
from rest_framework import serializers
from .models import (
    Song,
    Podcast,
    Audiobook,
)

utc = pytz.UTC

class Validators:
    @staticmethod
    def validate_datetime(value):
        curr_time = datetime.now(tz=None)
        if utc.localize(value) < utc.localize(curr_time):
            raise serializers.ValidationError('Upload time cannot be in the past')

    @staticmethod
    def validate_participants(participants):
        if len(participants) > 10:
            raise serializers.ValidationError('Participants should not be more than 10')

class SongFileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    duration_in_secs = serializers.IntegerField(min_value=0)
    uploaded_time = serializers.DateTimeField(validators=[Validators.validate_datetime])

    def create(self, data):
        song_obj = Song.objects.create(**data)
        return song_obj

    def update(self, instance, data):
        instance.update(**data)
        return data

class PodcastFileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    duration_in_secs = serializers.IntegerField(min_value=0)
    uploaded_time = serializers.DateTimeField(validators=[Validators.validate_datetime])
    host = serializers.CharField(max_length=100)
    participants = serializers.JSONField(validators=[Validators.validate_participants])

    def create(self, data):
        podcast_obj = Podcast.objects.create(**data)
        return podcast_obj
    def update(self, instance, data):
        instance.update(**data)
        return data


class AudiobookFileSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=10)
    duration_in_secs = serializers.IntegerField(min_value=0)
    uploaded_time = serializers.DateTimeField(validators=[Validators.validate_datetime])
    author = serializers.CharField(max_length=100)
    narrator = serializers.CharField(max_length=100)

    def create(self, data):
        audiobook_obj = Audiobook.objects.create(**data)
        return audiobook_obj
    def update(self, instance, data):
        instance.update(**data)
        return data

