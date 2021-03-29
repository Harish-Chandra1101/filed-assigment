from .serializers import (
    SongFileSerializer,
    PodcastFileSerializer,
    AudiobookFileSerializer,
)
from .models import (
    Song,
    Podcast,
    Audiobook,
)
from utils.responses import GenericResponse
from .constants import VALID_FILE_TYPES


class AudioFileHandler:

    @staticmethod
    def create_audio_file(request):
        file_type = request.data.get('audioFileType') or ''
        serializer_class = AudioFileHandler.get_serializer_class(file_type)
        if not serializer_class:
            return GenericResponse.get_error_response(
                msg='Invalid File type'
            )
        file_data = request.data.get('audioFileMetadata') or {}
        serial_obj = serializer_class(data=file_data)
        if serial_obj.is_valid():
            serial_obj.save()
            return GenericResponse.get_success_response(
                data=f"Audio file of type {file_type} created"
            )
        return GenericResponse.get_error_response(
            msg=serial_obj.errors
        )

    @staticmethod
    def update_audio_file(request, url_args):
        file_type = url_args.get('audioFileType') or ''
        file_id = url_args.get('audioFileID')
        file_data = request.data.get('audioFileMetadata') or {}
        if not file_id:
            return GenericResponse.get_error_response(
                msg='File id not provided'
            )
        elif not file_type or file_type not in VALID_FILE_TYPES:
            return GenericResponse.get_error_response(
                msg='File type invalid'
            )
        model = {
            'Song': Song,
            'Podcast': Podcast,
            'Audiobook': Audiobook,
        }.get(file_type)
        audio_file = model.objects.filter(pk=file_id)
        if not audio_file:
            return GenericResponse.get_error_response(
                msg=f'Audio file {file_type} not found with id {file_id}'
            )
        serializer_class = AudioFileHandler.get_serializer_class(file_type)
        serial_obj = serializer_class(audio_file, data=file_data, partial=True)
        if serial_obj.is_valid():
            serial_obj.save()
            return GenericResponse.get_success_response(
                data=file_data
            )
        return GenericResponse.get_error_response(
            msg=serial_obj.errors
        )

    @staticmethod
    def get_serializer_class(file_type):
        serializer_class = {
                               'Song': SongFileSerializer,
                               'Podcast': PodcastFileSerializer,
                               'Audiobook': AudiobookFileSerializer,
                           }.get(file_type) or None
        return serializer_class

